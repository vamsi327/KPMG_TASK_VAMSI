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


# alternate 3
task2-Instance-metadata.cs , worthy script - not hand written -but wish i could try this as per the code i observe

# KPMG TASK 3 

ALERNATE SOLUTION

var object = {"a1": { "b1": { "c1": "d1" }}};

console.log("Result at 'a1.b1.c1': ",_.get(object, 'a1.b1.c1'));
console.log("Result at 'a1.b1.nonexistent key': ",_.get(object, 'a1.b1.nonexistent', "default result"));

var object2 = {"x1":{"y1":{"z1":"a1"}}};
console.log("Result at 'x1.y1.z1': ",_.get(object2, 'x1.y1.z1'));

<script src="https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.11/lodash.js"></script>

