import pyglet
from pyglet.window import key
import time
import random
import csv

# Set up Stimuli and Responses
colors = {'red': (255, 0, 0, 255), 'green': (0, 255, 0, 255), 'blue': (0, 0, 255, 255)}
color_names = list(colors.keys())
key_responses = {key.LEFT: 'red', key.DOWN: 'green', key.RIGHT: 'blue'}

# Initialize Window, Text Label, and Keyboard Input
window = pyglet.window.Window()
window.dispatch_events()
text = pyglet.text.Label('Hello', font_size=64, y=200, x=200)
keyboard = key.KeyStateHandler()
window.push_handlers(keyboard)

# Open Log File
with open('myfile.csv', 'w') as f:

	writer = csv.DictWriter(f, ['Trial', 'WordText', 'WordColor', 'Response', 'ResponseTime'])
	writer.writeheader()

	# Main Experiment Loop
	for trialnum in range(1, 201):
		
		window.clear()
		time.sleep(.3)

		# Randomly Select Trial's Text and Color
		word = random.choice(color_names)
		if random.randrange(2):
			word_color = color_names[color_names.index(word) - random.randint(1, 2)]  
		else:
			word_color = word

		# Apply Text and Color to Label, then Draw
		text.text = word
		text.color = colors[word_color]
		text.draw()
		window.flip()

		# Collect Keyboard Response 
		start_time = time.time()
		response = ''
		keyboard.clear()
		start_time = time.time()
		while not response:
			window.dispatch_events()
			for pressed in keyboard:
				if keyboard[pressed] and pressed in key_responses:
					response = key_responses[pressed]
					response_time = time.time() - start_time
					print(response, response_time)
			if key.ESCAPE in keyboard:
				window.close()

			
		# Log the Trial to File
		trial = {'Trial': trialnum, 
				 'WordText': word, 
				 'WordColor': word_color, 
				 'Response': response, 
				 'ResponseTime': response_time}
		writer.writerow(trial)