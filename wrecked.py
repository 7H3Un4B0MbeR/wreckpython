import subprocess
import time

def run_command(command, shell=True):
    """Helper function to run a shell command and print its output."""
    result = subprocess.run(command, shell=shell, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {command}")
        print(result.stderr)
    else:
        print(result.stdout)
    return result

def main():
    try:
        # Step 1: Kill existing frida-server process
        print("Killing existing frida-server process...")
        run_command("adb shell su -c pkill -9 frida-server")

        # Step 2: Set SELinux to permissive mode
        print("Setting SELinux to permissive mode...")
        run_command("adb shell su -c setenforce 0")

        # Step 3: Start frida-server in the background
        print("Starting frida-server...")
        subprocess.Popen("adb shell su -c '/data/local/tmp/frida-server-16.6.6-android-arm64 &'", shell=True)

        # Wait for frida-server to start
        print("Waiting for frida-server to initialize...")
        subprocess.Popen("adb shell 'ps -A | grep frida-server'")


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
