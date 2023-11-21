# gRPC and protocol buffer in python

gRPC allows clients and server applications to communicate more efficiently on a connected system.

Example:
Create the `rides.proto` file as follow:

```protobuf
syntax = "proto3";

message StartRequest {
    int64 car_id = 1;
    string driver_id = 2;
    repeated string passenger_ids = 3;
}
```

Execute: `protoc --python_out=. rides.proto`
It will generate a new file: `rides_pb2.py`.
Create the `marshalling.py` file as follow:

```python
import rides_pb2 as pb


request = pb.StartRequest(
    car_id=95,
    driver_id="McQueen",
    passenger_ids=["p1", "p2", "p3"]
)
print(request)
# region Marshal
data = request.SerializeToString()
print("type: ", type(data))
print("size: ", len(data))
# endregion

# region Unmarshal
request2 = pb.StartRequest()
request2.ParseFromString(data)
print(request2)
# endregion
```

Execute: `python marshalling.py`
