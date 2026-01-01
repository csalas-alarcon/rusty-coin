/// factorial implemented with an iterator
fn factorial_iter(num: usize) -> usize {
    (1..num)
    .fold(1, |acc, x| acc* x)
}
/// factorial implemented with a loop and a mutable variable
fn factorial_loop(num: usize) -> usize {
    let mut sum= 1;
    for x in 2..num {
        sum*= x;
    }
    sum
}
/// fibonacci implementation with a loop
fn fibonacci(n: usize) -> usize {
    let mut a= 1;
    let mut b= 1;

    for _ in 1..n{
        let old_a= a;
        a= b;
        b+= old_a;
    }
    b
}

fn main() {
    let x= factorial_iter(12);
    let y= factorial_loop(20);
    let fib= fibonacci(35);
    println!("Factorial 1: {}, Factorial 2: {}, fibbonaci: {}", x, y, fib);
}

