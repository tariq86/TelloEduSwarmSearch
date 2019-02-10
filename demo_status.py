from fly_tello import FlyTello
my_tellos = list()


#
# SIMPLE EXAMPLE - MOST BASIC FLIGHT TO SHOW STATUS MESSAGES
#
# SETUP: Any number of Tellos
#


#
# MAIN FLIGHT CONTROL LOGIC
#

# Define the Tello's we're using, in the order we want them numbered
my_tellos.append('0TQDFC6EDBBX03')
my_tellos.append('0TQDFC6EDB4398')

# Control the flight
with FlyTello(my_tellos, get_status=True) as fly:
    fly.print_status(sync=True)
    fly.takeoff()
    fly.print_status(sync=True)
    fly.land()
    fly.print_status(sync=True)
