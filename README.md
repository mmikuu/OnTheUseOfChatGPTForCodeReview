# Replication package for "On the Use of ChatGPT for Code Review"
This repository includes the replication package and results for EASE2024 (Short Paper). 
If you want to use this tool in your research, please cite the following papers:
```
To appear after the acceptance
```

## Source code
 Our main source code is located in 'chatgpt_review' directory.

### Require
・Docker(> 24.0.5)

### Run
This program is designed to run on docker. 
A python program will be executed by Docker compose.<br>

1. You need to obtain GitHub tokens
2. Write the obtained tokes in tokens.txt
3. You can run it with the following commands:
```
docker-compose build
docker-compose up
```
Note: To collect new data, you need to modify docker-compose.yml so that it can run main1_get_data.py. 
### Outputted file 
The program will generate "results/links.csv" that contains the list of the links for each discussion including ChatGPT sharing links. 

## Annotated results
With the output of the above program, two of the authors performed the manual inspection independently and manually. 
The annotated classification result is stored in the "results/annotations/classification.csv" file. 