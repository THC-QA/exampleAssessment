#!/usr/bin/env python3
def endsPy(input):
	list_in = list(input.lower())
	if list_in[-1] == "y" and list_in[-2] == "p":
		return True
	else:
		return False