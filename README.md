# KPMG_TASK 1
USAGE:

Take a copy of terraform.tfvars.template and substitute required values.

Apply as i.e. terraform apply -var-file=terraform.tfvars


# KPMG_TASK 2
Reference sources :
https://aws.amazon.com/blogs/developer/ec2metadata/

for inducvidual meta data , i usually  take the response body of this request, parse with with json  library 

wget -q -O - http://169.254.169.254/latest/meta-data

# or as an alternative we can use mentioned python script.
python task2-python-approach.py  <( aws ec2 describe-instances  )
python task2-python-approach.py  <( aws ec2 --region us-east-2 describe-instances  )
python task2-python-approach.py <( aws ec2 --region us-east-2 describe-instances  ) | column -t | sort -k1,1 | cat -n  | grep running  
