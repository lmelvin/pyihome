# pyihome

Python library to interface with the iHome API.

This library interfaces with the [EVRYTHING API](https://developers.evrythng.com/reference)

Currently this library supports the following:

All Devices
 - get devices associated with the account which are swtiches with only one outlet

Switch
 - turn_on(*device_id*)
 - turn_off(*device_id*)
 - get_state(*device_id*)

How to use

```python
from pyihome import PyiHome

#init api
api = PyiHome("username", "password")

#get devices
devices = api.get_devices()

#get device id of the first item
device_id = devices[0]["id"]

#get switch specific api
switch = api.Switch()

#turn on the switch
switch.turn_on(device_id)

#turn off the switch
switch.turn_off(device_id)

#get state
print("State: {}".format(switch.get_state(device_id)))
```
