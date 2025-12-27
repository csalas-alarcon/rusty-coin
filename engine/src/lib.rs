use pyo3::prelude::*;
use std::collections::HashMap;

/// This function will be visible in Python
#[pyfunction]
fn count_letters(text: String) -> PyResult<HashMap<char, usize>> {
    let mut counts = HashMap::new();

    for c in text.chars() {
        // We only care about letters (this works for Arabic characters too!)
        if c.is_alphabetic() {
            *counts.entry(c).or_insert(0) += 1;
        }
    }

    Ok(counts)
}

/// This defines the Python module name
#[pymodule]
fn quran_engine(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(count_letters, m)?)?;
    Ok(())
}