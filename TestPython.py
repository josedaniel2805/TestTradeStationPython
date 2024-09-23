import requests
import json

def check_github_status():
    url = "https://www.githubstatus.com/api/v2/summary.json"
    
    try:
        # Make an HTTP GET request to fetch the raw JSON file
        response = requests.get(url)
        
        # Raise an error if the request was unsuccessful
        response.raise_for_status()

        # Load the response text as JSON
        data = response.json()

        overall_status = data["status"]["description"]

        incidents = data["incidents"]

        if(len(incidents) < 1):
            print(overall_status)
        else:
            print("The following incidents are on going:")
            for val in incidents:
                print(json.dumps(val, indent=2))  

            components = data["components"]

            failed_component = []

            for val in components:
                if val["status"] != "operational":
                    failed_component.append(val)

            print(f"GitHub is experiencing: {len(failed_component)} issue(s) on the following components:")
            for val2 in failed_component:
                print(f"Component Name: {val2["name"]}")
                print(f"Component Description: {val2["description"]}")
                print(f"Component Status: {val2["status"]}")
                #in case that you would like to see all the attributes uncomment the next line
                #print(json.dumps(val2, indent=2))
        

    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error connecting to the GitHub Status API. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("The request to the GitHub Status API timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except ValueError:
        print("Error decoding JSON response.")

if __name__ == "__main__":
    check_github_status()
