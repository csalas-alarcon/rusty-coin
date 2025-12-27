import flet as ft 
import quran_engine

def main(page: ft.Page):
    # Setup for Arabic Support
    page.title = "Quran Reader Engine"
    page.theme_mode = ft.ThemeMode.DARK  # Fixed case
    page.rtl = True
    page.scroll = "adaptive"  # Fixed spelling

    # UI Components
    content_display = ft.Text(size=18, selectable=True)
    stats_display = ft.Column()

    def handle_file_picker(e): # Fixed spelling
        if e.files:
            file_path = e.files[0].path 
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    text = f.read()

                    # 1. Update the UI with the text
                    content_display.value = text 

                    # 2. Use the RUST engine to calculate the stats
                    char_counts = quran_engine.count_letters(text)

                    # 3. Update stats UI
                    stats_display.controls.clear() # Clear old results
                    stats_display.controls.append(ft.Text("Top Letters:", weight="bold"))
                    
                    # Sort by frequency and show top 10
                    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
                    for char, count in sorted_counts[:10]:
                        stats_display.controls.append(ft.Text(f"{char}: {count}"))
                    
                    page.update()

            except Exception as ex:
                print(f"Error: {ex}")
    
    # 1. Setup the picker (Hidden)
    file_picker = ft.FilePicker()
    file_picker.on_result = handle_file_picker
    page.overlay.append(file_picker) # This keeps it "invisible" until called

    # 2. Add visible UI
    page.add(
        ft.Row([ft.Text("Empire File Viewer", size=32, weight="bold")], alignment=ft.MainAxisAlignment.CENTER),
        ft.FilledButton(
            "Select Arabic .txt File", 
            on_click=lambda _: file_picker.pick_files(allowed_extensions=["txt"])
        ),
        ft.Divider(),
        ft.Row([
            ft.Container(content=content_display, expand=3, padding=20),
            ft.VerticalDivider(),
            ft.Container(content=stats_display, expand=1)
        ], vertical_alignment=ft.CrossAxisAlignment.START)
    )

if __name__ == "__main__":
    ft.run(main)