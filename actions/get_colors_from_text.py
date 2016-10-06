from st2actions.runners.pythonrunner import Action
from lib import colors 

class EvaluateTweetAction(Action):
    def run(self, text):
        rgb_colors = colors.Colors.search_for_color_in_text(text)
        if rgb_colors:
            results = {
                'red': rgb_colors[0],
                'green': rgb_colors[1],
                'blue': rgb_colors[2]
            }
            return (True, results)

        return (False, "No colors found!")
