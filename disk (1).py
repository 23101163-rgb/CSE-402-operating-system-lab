requests=[3,60,10,25,30,4]
current_head=41
total_head_movement=0
seek_sequence=[]
pending_requests=list(requests)
print("SSTF=")
while pending_requests:
     closest_request=min(pending_requests,key=lambda req:abs(current_head-req))
     distance=abs(current_head-closest_request)
     total_head_movement+=distance
     current_head=closest_request
     seek_sequence.append(closest_request)
     pending_requests.remove(closest_request)
print(total_head_movement)
print(seek_sequence)
print("FCFS=")

total_head_movement=0
current_head=41
seek_sequence=[]
for request in requests:
    distance = abs(current_head - request)
    total_head_movement += distance
    seek_sequence.append(request)
    current_head=request
print(total_head_movement)
print(seek_sequence)
