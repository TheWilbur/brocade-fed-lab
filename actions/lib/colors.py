import re

class Colors(object):
    colors = {
        "maroon": [128,0,0],
        "brown": [165,42,42],
        "crimson": [220,20,60],
        "red": [255,0,0],
        "tomato": [255,99,71],
        "coral": [255,127,80],
        "salmon": [250,128,114],
        "orange": [255,165,0],
        "gold": [255,215,0],
        "khaki": [240,230,140],
        "olive": [128,128,0],
        "yellow": [255,255,0],
        "green": [0,128,0],
        "lime": [0,255,0],
        "teal": [0,128,128],
        "aqua": [0,255,255],
        "cyan": [0,255,255],
        "turquoise": [64,224,208],
        "navy": [0,0,128],
        "blue": [0,0,255],
        "indigo": [75,0,130],
        "purple": [128,0,128],
        "thistle": [216,191,216],
        "plum": [221,160,221],
        "violet": [238,130,238],
        "magenta": [255,0,255],
        "fuchsia": [255,0,255],
        "orchid": [218,112,214],
        "pink": [255,192,203],
        "beige": [245,245,220],
        "bisque": [255,228,196],
        "wheat": [245,222,179],
        "sienna": [160,82,45],
        "chocolate": [210,105,30],
        "peru": [205,133,63],
        "tan": [210,180,140],
        "linen": [250,240,230],
        "lavender": [230,230,250],
        "honeydew": [240,255,240],
        "ivory": [255,255,240],
        "azure": [240,255,255],
        "snow": [255,250,250],
        "black": [0,0,0],
        "gray": [128,128,128],
        "grey": [128,128,128],
        "silver": [192,192,192],
        "white": [255,255,255]
    }

    @staticmethod 
    def search_for_color_in_text(text):
	''' Search a text for a color. Returns an RGB set of values if of the first color found, or None if not found '''  

        # Split up the words and punctuation into a array
        words_and_punctuation = re.findall(r"[\w']+|[.,!?;]", text)

        # Interate through each element
        for each in words_and_punctuation:

             # See if words are colors, but skip the lookup if length
             # is less than 3 since there are no colors.
             if len(each)>2 and each.lower() in Colors.colors:
                  return Colors.colors[each.lower()]

        # No matches found, so return None
        return None

if __name__ == "__main__":
    # Validation data
    print(Colors.search_for_color_in_text("I'd like to see the lab in Red!"))
    print(Colors.search_for_color_in_text("Blue is my favorite color"))
