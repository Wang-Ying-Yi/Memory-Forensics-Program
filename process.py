import subprocess
import time

def collect_ram_data(output_file):
    # Use WinPMEM to collect RAM data from the host Windows system.
    # Note: This will need to be executed on Windows, not within WSL.
    winpmem_path = "winpmem_mini_x64_rc2"
    subprocess.run([winpmem_path, output_file])
    print("RAM data collected using WinPMEM.")

def access_disk_image_with_volatility3(image_path):
    # Access the RAM image using Volatility3's windows plugins
    plugins = [
        "windows.pslist.PsList"
    ]
    
    for plugin in plugins:
        cmd = ["python", "[The Access to~\Assessment2\\volatility3\\vol.py]"
, "-f", image_path, plugin]
        subprocess.run(cmd)

def main():
    ram_output_file = "memory_dump.raw"

    # Task 1: Conduct RAM Forensic Data Acquisition (Data Acquisition)
    collect_ram_data(ram_output_file)

    # Wait for 2 seconds
    time.sleep(2)

    # Task 2: For simplicity, using the raw RAM dump directly for analysis with Volatility3.

    # Task 3: Access the RAM image using Volatility3 (Disk Image Access)
    access_disk_image_with_volatility3(ram_output_file)

if __name__ == "__main__":
    start_time = time.time()

    # Execute the tasks
    main()

    end_time = time.time()
    running_time = end_time - start_time

    # Task 4: Calculate the running time of the program (Program Running Time)
    print(f"Program ran for {running_time:.2f} seconds.")