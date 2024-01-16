import requests

class CostReportError(Exception):
    pass

def cost_rep(access_token, scope, granularity, filter_name, filter_value, type='ActualCost', timeframe= 'MonthToDate',sorting='descending', sort_by= 'Cost'):
    
    cost_management_endpoint = f"https://management.azure.com/{scope}/providers/Microsoft.CostManagement/query?api-version=2023-11-01"

    headers = {
            'Authorization': 'Bearer ' + access_token,
            'Content-Type': 'application/json'
        }
    

    body =  {
        "type": type,
        "timeframe": timeframe, 
        "dataset": {
            "granularity": granularity,
            "aggregation": {
                "totalCost": {
                    "name": "Cost",
                    "function": "Sum"
                }
            },
            "sorting": [
                {
                    "direction": sorting,
                    "name": sort_by
                }
            ],
            "grouping": [
                {
                    "type": "Dimension",
                    "name": "ServiceName"
                },
            ],
            "filter": {
                "Dimensions": {
                    "name": filter_name,
                    "Operator": "In",
                    "values": filter_value
                },
            }
        }
    }
    
    
    try:
        response = requests.post(cost_management_endpoint, headers=headers, json=body)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as req_err:
        raise CostReportError(f"Error during request: {req_err}")
    
    except ValueError as json_err:
        raise CostReportError(f"Error decoding JSON response: {json_err}")
    
    except Exception as e:
        raise CostReportError(f"Unexpected error: {e}")
