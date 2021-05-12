import json
import sys

with open( sys.argv[1] ) as f:
  aws = json.load( f ) 
  Reservations = aws['Reservations']
  for Reservation in Reservations:
    Instances = Reservation['Instances']
    for Instance in Instances:
      Tags = Instance['Tags']
      for Tag in Tags:
        if Tag['Key'] == "Name":
          print Tag['Value'],Instance['PrivateIpAddress'],Instance['InstanceId'],Instance['State']['Name']
