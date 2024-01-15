import requests

class metrics_Error(Exception):
    pass

def res_metrics(access_token, scope, resource_info, metricNames, timeRange):

    resourceProviderNamespace = resource_info[0]
    resourceType = resource_info[1]
    resourceName = resource_info[2]

    headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }

    metrics_url = f"https://management.azure.com/{scope}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}/providers/microsoft.insights/metrics?api-version=2018-01-01&metricnames={metricNames}&timespan={timeRange}"

    try:
        metrics_response = requests.get(metrics_url, headers=headers)
        metrics_response.raise_for_status()
        return metrics_response.json()
    
    except requests.exceptions.RequestException as req_err:
        raise metrics_Error(f"Error during request: {req_err}")
    
    except ValueError as json_err:
        raise metrics_Error(f"Error decoding JSON response: {json_err}")
    
    except Exception as e:
        raise metrics_Error(f"Unexpected error: {e}")
