# Pre-requisites
- Create an account at [Instill Tech](https://www.instill.tech)

# Implementation
## How to run dinner-jia-sa with API
- Set the `INSTILL_API_TOKEN` env variable in terminal:
```
$ export INSTILL_API_TOKEN=********
```


## Run `joycelyn/dinner-jia-sa` using API.
```
curl -X POST 'https://api.instill.tech/v1beta/users/joycelyn/pipelines/dinner-jia-sa/trigger' \
--header "Content-Type: application/json" \
--header "Authorization: Bearer $INSTILL_API_TOKEN" \
--data '{
  "inputs": [
    {
      "main": "Please put your value here",
      "protein": "Please put your value here",
      "style": "Please put your value here",
      "temp": "Please put your value here",
      "time": "Please put your value here"
    }
  ]
}'

```

## Demo
![Dinner Jia Sa demo](imgs/pipeline-demo.png?raw=true)
- Or [try it for yourself](https://instill.tech/joycelyn/pipelines/dinner-jia-sa/playground). 