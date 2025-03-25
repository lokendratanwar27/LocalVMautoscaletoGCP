import time
import multiprocessing

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():
    """Continuously generate prime numbers"""
    num = 2  # Start from 2
    while True:
        if is_prime(num):
            pass  # Do nothing, just keep checking
        num += 1

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()  # Get number of CPU cores
    print(f"Starting stress test on {num_cores} CPU cores...")

    processes = []
    for _ in range(num_cores):  # Use all CPU cores
        p = multiprocessing.Process(target=generate_primes)
        p.start()
        processes.append(p)

    try:
        # Run stress test for 2 minutes
        time.sleep(120)
    except KeyboardInterrupt:
        print("\nStress test stopped by user.")
    finally:
        # Terminate all processes
        for p in processes:
            p.terminate()
        print("Stress test completed.")
