# Mutility: Windows System Utility Toolkit

---

![Mutility Screenshot](https://raw.githubusercontent.com/llllmithulllll/Mutility/Mutility.png)


## Introduction

Mutility is a powerful and intuitive **Python-based GUI application** designed to simplify common Windows system maintenance, optimization, and management tasks. Built with `tkinter`, it offers a centralized dashboard to streamline operations that typically require multiple steps or command-line interactions. This tool is perfect for users who want to automate repetitive tasks, optimize system performance, and access a wide range of essential Windows functionalities from one convenient interface.

---

## Features

Mutility helps you take control of your Windows system with a single click, providing features such as:

* **Windows Update Control:** Easily enable or disable automatic Windows updates.
* **Windows Defender Management:** Toggle real-time monitoring for Windows Defender on or off.
* **System Cleanup:** Quickly clear temporary files to free up disk space.
* **Windows Debloating:** Run scripts to remove unnecessary pre-installed applications and telemetry, both from local files or an up-to-date online source.
* **Software Management:** Install and uninstall the **Chocolatey** package manager (and ChocolateyGUI), and quickly install popular browsers like **Google Chrome** and **Brave** using `winget`.
* **Advanced System Tools:** Access options for uninstalling the **Microsoft Store**, initiating a **factory reset** of Windows, and performing online **system health checks**.
* **MS Tool Kit (Activation):** Direct access to the Microsoft Toolkit application.

---

## Requirements

To run Mutility, you need the following:

* **Operating System:** Windows 10 or Windows 11.
* **Python:** Python 3.x installed on your system.
    * `tkinter` module (usually included with standard Python installations).
* **PowerShell:** Windows PowerShell (built-in).
* **Administrator Privileges:** The application performs system-level operations, so it **must be run as an Administrator**.
* **Internet Connection:** Required for "Online Debloater," "Install Chocolatey," "Install Chrome," "Install Brave," and "Online System Restore" features.
* **App Installer / Winget:** For browser installations, ensure that "App Installer" (which includes `winget`) is installed and up to date on your Windows system.
* **External Files & Directory Structure:** The application relies on several external PowerShell scripts and executables. These ***must*** be placed in a `Data` subdirectory relative to where `mutility.py` (your Python script) is located.

    Your directory structure should look like this:

    ```
    Mutility_App/
    ├── mutility.py
    └── Data/
        ├── Windows10Debloater-master/
        │   └── Windows10DebloaterGUI.ps1
        ├── choco-develop/
        │   └── setup.ps1
        ├── uninstall_store.ps1
        ├── Win-Debloat-Tools-main/
        │   └── Win10ScriptGUI.ps1
        └── Microsoft_toolkit_setup/
            └── Microsoft Toolkit.exe
    ```

    **Note:** The exact content of `Windows10Debloater-master`, `choco-develop`, `Win-Debloat-Tools-main`, and `Microsoft_toolkit_setup` should be the respective project files from their original sources.

---

## Installation & Setup

1.  **Download/Clone:** Obtain the `mutility.py` script and the necessary external files.
2.  **Organize Files:** Create a directory (e.g., `Mutility_App`). Place `mutility.py` directly inside this directory. Then, create a subdirectory named `Data` within `Mutility_App`. Populate the `Data` directory with the required external scripts and tools as specified in the [Requirements](#requirements) section.
3.  **PowerShell Execution Policy:** For PowerShell scripts to run, you might need to adjust your PowerShell execution policy. The application attempts to set `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` at startup, which is generally safe for local scripts. If you encounter issues, you may need to manually adjust it by opening PowerShell **as Administrator** and running:
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    Confirm with 'Y' if prompted.
4.  **Run the Application:**
    * Navigate to the `Mutility_App` directory in your File Explorer.
    * Right-click on `mutility.py` and select "**Run as administrator**."
    * Alternatively, open Command Prompt or PowerShell, navigate to the `Mutility_App` directory, and run:
        ```bash
        python mutility.py
        ```
        (Ensure your terminal is running as administrator).

---

## Usage

Once the Mutility application window appears, simply click on the respective buttons to perform the desired action.

* **Buttons on the Left Column:** Primarily for Windows Update and Defender control, and uninstalling MS Store.
* **Buttons in the Middle Column:** For Chocolatey management, temporary file cleanup, and Windows debloating.
* **Buttons on the Right Column:** For Windows Reset, browser installation, downloading applications, and system health checks.
* **Credits Button:** Provides information about the developer.
* **MS Tool Kit Button:** Opens the Microsoft Toolkit application.

**Always pay attention to the pop-up messages (labeled "Attention") and your console/terminal window, as some operations provide crucial feedback or require interaction there.**

---

## Important Notes & Warnings

* **Administrator Privileges are Crucial:** Most operations performed by this tool require elevated permissions. Running it without administrator rights will result in "Access Denied" errors.
* **System Modifications:** This tool makes significant changes to your operating system. Use it with extreme caution.
* **Debloating:** Windows debloating scripts can remove applications you might use. Understand what a script does before running it.
* **Microsoft Toolkit:** The "MS Tool Kit (Activation)" button opens a third-party tool that may have legal implications regarding software licensing. Use at your own discretion and responsibility.
* **Winget/App Installer:** Ensure your Windows App Installer is up-to-date for `winget` commands to function correctly (for browser installations).
* **Internet Connection:** Several features rely on an active internet connection to download or execute online scripts.

---

## Troubleshooting

* **"Access Denied" Errors:**
    * **Solution:** Ensure you are running the `mutility.py` script **as Administrator**.
* **PowerShell Scripts Not Running / "Execution Policy" Errors:**
    * **Solution:** Manually set your PowerShell execution policy. Open PowerShell **as Administrator** and run `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`.
* **"File Not Found" Errors:**
    * **Solution:** Verify that your `Data` directory is correctly structured and contains all the necessary external scripts and executables as described in the [Requirements](#requirements) section. Ensure file names match exactly.
* **"Winget is not recognized..." (for Chrome/Brave):**
    * **Solution:** Make sure your Windows App Installer is installed and up-to-date. You might need to update Windows or install App Installer from the Microsoft Store.
* **`choco install chocolateygui` fails after `setup.ps1`:**
    * **Reason:** Chocolatey might not be immediately available in the system's PATH after its initial setup script runs.
    * **Potential Solution:** You might need to restart the application or open a new terminal for Chocolatey to be recognized after installation.

---

## Credits

Developed by **Mithlesh**
* **Instagram:** [@mithlesh1144](https://www.instagram.com/mithlesh1144)
* **Github:** [github.com/llllmithulllll](https://github.com/llllmithulllll)
* **LinkedIn:** [www.linkedin.com/in/mithlesh1144/](https://www.linkedin.com/in/mithlesh1144/)

---

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
