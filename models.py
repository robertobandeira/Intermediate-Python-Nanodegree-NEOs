"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation = '', name = None, diameter = float('nan'), hazardous = False):
        """Create a new `NearEarthObject`.

        :param designation: The primary designation for this NearEarthObject
        :param name: The IAU name for this NearEarthObject
        :param diameter: The diameter, in kilometers, of this NearEarthObject
        :param hazardous: Whether or not this NearEarthObject is potentially hazardous
        """
        self.designation = designation
        self.name = name if name != '' else None
        if diameter is None or diameter == '':
            self.diameter = float('nan')
        else:
            self.diameter = diameter
        self.hazardous = True if hazardous == 'Y' else False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name == None:
            return f"{self.designation}"
        else:
            return f"{self.designation} ({self.name})"

    def __str__(self):
        """Return `str(self)`."""
        not_s = ' not' if self.hazardous == False else ''
        return f"NEO {self.fullname} has a diameter of {self.diameter:.3f} km and is{not_s} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation = '', time = None, distance = 0.0, velocity = 0.0):
        """Create a new `CloseApproach`.

        :param time: The date and time, in UTC, at which the NEO passes closest to Earth.
        :param distance: The nominal approach distance, in astronomical units, of the NEO to Earth at the closest point.
        :param valocity: The velocity, in kilometers per second, of the NEO relative to Earth at the closest point.
        :param neo: The NearEarthObject that is making a close approach to Earth.
        """
        self._designation = designation
        self.time = cd_to_datetime(time) if time is not None else None
        if distance is None or distance == '':
            self.distance = 0.0
        else:
            self.distance = float(distance)
        if velocity is None or velocity == '':
            self.velocity = 0.0
        else:
            self.velocity = float(velocity)
        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time) if self.time is not None else ''

    def __str__(self):
        """Return `str(self)`."""
        return f"At {self.time_str}, '{self._designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
