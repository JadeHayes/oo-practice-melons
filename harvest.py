############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = True
        self.is_bestseller = True
        self.name = name
        self.pairings = []

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # add the instances pairing to the list pairings
        self.pairings.extend([pairing])

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        # the old code is going tobe switched out with the newcode
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""
    # Instansiate different melons on the class melon type
    melon_types = []
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')

    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermelon.add_pairing('ice cream')

    melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    # loop through the different objects in melon_types list
    for obj in melon_types:
        print "{} pairs nicely with ".format(obj.name)
        # Ask hackbright about an easier way to do this
        if len(obj.pairings) > 1:
            print "- {}".format(obj.pairings[0])
            print "- {}".format(obj.pairings[1]), "\n"
        else:
            print "- {}".format(" ".join(obj.pairings)), "\n"


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    # Fill in the rest
    ans = {}

    for obj in melon_types:
        ans[obj.code] = [obj.first_harvest, obj.color, obj.is_seedless, obj.is_bestseller,
                         obj.name]
    print ans
    return ans

############
# Part 2   #
############


class Melon(object):
    """A melon in a melon harvest."""
    # Fill in the rest
    # Needs __init__ and is_sellable methods
    #Initializing melons
    def __init__(self, melon_types, shape_rating, color_rating, field, harvester):
        self.melon_types = melon_types
        self. shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvester = harvester
        self.is_sellable = False


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_obj = []

    melon_1 = Melon(melon_types['yw'], 8, 7, 2, 'Sheila')
    melon_2 = Melon(melon_types['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melon_types['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melon_types['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melon_types['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melon_types['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melon_types['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melon_types['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melon_types['yw'], 7, 10, 3, 'Michael')

    melon_obj.extend([melon_1, melon_2, melon_3, melon_4, melon_5,
                      melon_6, melon_7, melon_8, melon_9])
    print melon_obj
    return melon_obj


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.shape_rating > 5 and melon.color_rating > 5 and melon.field != 3:
            melon.is_sellable = True
        print melon.harvester, melon.field, melon.is_sellable
