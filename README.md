# pyihome

Python library to interface with the iHome API.

This library interfaces with the [EVRYTHING API](https://developers.evrythng.com/reference)

How to use

```python
from pyihome import PyiHome

# init api
api = PyiHome("username", "password")

# get ALL devices
# note this is a json object
devices = api.devices

# get ALL switches
switches = api.switches

# work with a single switch
switch = switches[0]

# turn on the switch
switch.turn_on()

# turn off the switch
switch.turn_off()
```

### Switch

**Properties**

| Property      | Type          |
| ------------- |:------------- |
| name          | str           |
| id            | str           |

**Methods**

| Method        | Params        | Return Type | Description                                             |
| ------------- | ------------- | ----------- | ------------------------------------------------------- |
| turn_on()     |               | None        | Turns the switch on                                     |
| turn_off()    |               | None        | Turns the switch off                                    |
| get_state()   |               | int         | Gets the current state of the switch. 1 is on, 0 is off |
