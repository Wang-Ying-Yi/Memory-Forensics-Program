# Memory Forensics: Automated RAM Data Acquisition and Analysis
## Overview
This project involves the development of an automated system for the acquisition and analysis of Random Access Memory (RAM) data for digital forensics purposes. The application is designed to streamline the process of memory forensics by automatically capturing and analyzing volatile memory from Windows operating systems using Python.

![image](https://github.com/Wang-Ying-Yi/Memory-Forensics-Program/assets/81617593/f9d2d62b-7582-4f3b-bb68-abe26c8a674f)

## Features
+ Data Acquisition: Automates the capture of RAM data using WinPMEM.
+ Dump File Creation: Creates a dump file from the acquired RAM data for further analysis.
+ Memory Analysis: Utilizes Volatility 3 for in-depth analysis of the dump file to extract digital artifacts and important forensic data.
+ Performance Measurement: Evaluate the efficiency of the data acquisition and analysis process by calculating the running time of the program.

## Technologies Used
+ **VMWare Workstation Player:** Host platform for the operating system.
+ **Microsoft Windows:** Main operating system for program execution.
+ **Volatility 3:** Application for memory dump analysis.
+ **Python 3:** Core programming language used for developing the automated system.

## Installation and Setup
Ensure Python 3 and Volatility 3 are installed on your system. You can download WinPMEM from the official GitHub repository for capturing physical memory.

## Running the Application
1. Clone the repository.
2. Navigate to the project directory.
3. Run `python3 main.py` to start the automated memory forensics process.

## References
- [Crucial. (n.d.). What does computer memory (RAM) do?](https://www.crucial.com/articles/about-memory/support-what-does-computer-memory-do)
- [CPUU. (2023). An Introduction to Volatility 3 and installation guide. Cpuu-forensics.](https://cpuu.hashnode.dev/an-introduction-to-volatility-3)
- [Hausknecht, K., Foit, D., & Buric, J. (2015). RAM data significance in digital forensics. 2015 38th International Convention on Information and Communication Technology, Electronics and Microelectronics (MIPRO), 1372–1375.](https://doi.org/10.1109/MIPRO.2015.7160488)
- [Interpol. (n.d.). Digital forensics.](https://www.interpol.int/en/How-we-work/Innovation/Digital-forensics)
- [Kent, K., Chevalier, S., Grance, T., & Hung, D. (2006). Guide to Integrating Forensic Techniques into Incident Response. National Institute of Standards and Technology Special Publication 800-86.](https://doi.org/10.6028/NIST.SP.800-86)
- [Lord, N. (2020). What are memory forensics? A definition of memory forensics. Digital Guardian.](https://www.digitalguardian.com/blog/what-are-memory-forensics-definition-memory-forensics)
- [Thomas, T. P. (2023). WinPMEM | an open-source memory acquisition tool - TOJO P THOMAS - Medium. Medium.](https://medium.com/@tojopthomas/winpmem-an-open-source-memory-acquisition-tool-2b25c6eddeab)



