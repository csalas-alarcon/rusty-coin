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