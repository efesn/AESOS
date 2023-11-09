import subprocess
import requests
import webbrowser

def execute_python_file(file_path):
    with subprocess.Popen(["python", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
        out, err = proc.communicate()
    return out, err

def search_stackoverflow(query):
    resp = requests.get(
        "https://api.stackexchange.com/2.2/search",
        params={
            "order": "desc",
            "tagged": "python",
            "sort": "activity",
            "intitle": query,
            "site": "stackoverflow"
        }
    )
    return resp.json()

def open_stackoverflow_solutions(json_dict):
    url_list = []
    for item in json_dict['items']:
        if item['is_answered']:
            url_list.append(item["link"])
        if len(url_list) == 3:
            break

    for url in url_list:
        webbrowser.open(url)

def search_for_error_solutions(file_path):
    out, err = execute_python_file(file_path)
    error_message = err.decode("ISO-8859-1").strip().split("\r\n")[-1]

    if error_message:
        print(f"Error message: {error_message}")
        error_parts = error_message.split(":")
        json1 = search_stackoverflow(error_parts[0])
        json2 = search_stackoverflow(error_parts[1])
        json3 = search_stackoverflow(error_message)
        open_stackoverflow_solutions(json1)
        open_stackoverflow_solutions(json2)
        open_stackoverflow_solutions(json3)
    else:
        print("No error message found.")

if __name__ == "__main__":
    try:
        search_for_error_solutions(r"C:\Users\efesn\OneDrive\Masaüstü\X\AESOS\testfile.py")
    except Exception as e:
        print(f"Error: {str(e)}")
