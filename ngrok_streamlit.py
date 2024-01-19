from pyngrok import ngrok
import subprocess
import threading
import os

def stop_ngrok():
    ngrok_process = ngrok.get_ngrok_process()
    if ngrok_process:
        ngrok_process.proc.terminate()
        ngrok_process.proc.wait()
        print(" * ngrok tunnel stopped.")

    # Stop the Streamlit process
    streamlit_pid = os.getpid()  # Assuming you started Streamlit in the same script
    subprocess.Popen(["pkill", "-P", str(streamlit_pid)])
    print(" * Streamlit process stopped.")

def run_ngrok():
    # Run Streamlit in the background
    subprocess.Popen(["streamlit", "run", "app.py"])

    # Open a ngrok tunnel to the streamlit port 8501
    ngrok_tunnel = ngrok.connect(8501)

    # Print the ngrok tunnel URL
    print(" * ngrok tunnel \"{}\" -> \"http://127.0.0.1:{}/\"".format(ngrok_tunnel.public_url, 8501))

    # Wait for user input (or any other condition) to stop the ngrok tunnel
    input("Press Enter to stop the ngrok tunnel...")

    # Stop the ngrok tunnel when done
    stop_ngrok()

# Start the ngrok thread
ngrok_thread = threading.Thread(target=run_ngrok)
ngrok_thread.start()
