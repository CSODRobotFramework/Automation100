import json
import requests
import jsonpath


odics='{"K1":"val1","K2":"val2"}'
json_result = json.loads(odics)

print(json_result['K1'])

# Basic API GET Request
api_url="https://reqres.in/api/users?page=2"
response1= requests.get(api_url)
print(response1.text)

# Validate Status Code
assert response1.status_code==200

# Parse response into json format
json_response= json.loads(response1.text)
print(json_response)

# Apply json path
x=jsonpath.jsonpath(json_response,'total')
print(x[0])

y=jsonpath.jsonpath(json_response,'data[0].first_name')
print(y[0])

z=jsonpath.jsonpath(json_response,'data[2].last_name')
print(z[0])

# Fetch any data inside the json response for loop

for val in json_response['data']:
    print(val['first_name'])