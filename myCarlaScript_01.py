# ==============================================================================
# -- find carla module ---------------------------------------------------------
# ==============================================================================


import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

# ==============================================================================
# -- imports -------------------------------------------------------------------
# ==============================================================================
import carla

# ==============================================================================
# -- main ----------------------------------------------------------------------
# ==============================================================================
def main():
    try:
        # Use client to connect to server
        client = carla.Client('localhost', 2000)
        client.set_timeout(5.0)

        # Use client get world handle from server
        world = client.get_world()

        # Try to modify world weather
        weather = carla.WeatherParameters(cloudiness=10.0,
                                          precipitation=60.0,
                                          fog_density=10.0)
        world.set_weather(weather)
    finally:
        print("done")

if __name__ == '__main__':

    main()