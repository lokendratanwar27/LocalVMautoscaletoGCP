import multiprocessing
import time
import os

def stress_cpu():
    """Function to keep the CPU busy"""
    while True:
        pass  # Infinite loop to utilize CPU

if __name__ == "__main__":
    num_cores = os.cpu_count()  # Get number of CPU cores
    print(f"Starting stress test on {num_cores} CPU cores...")

    processes = []
    for _ in range(num_cores):  # Create a process for each core
        p = multiprocessing.Process(target=stress_cpu)
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
