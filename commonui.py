#!/usr/bin/python3.5

import tkinter as tk
'''
--------------------------------------------------------------------------------
	Desc: UI Common operation methods
--------------------------------------------------------------------------------
'''
class CommonUIOperation:
	'''
	--------------------------------------------------------------------------------
		Desc: Hide the Passed Widget
	--------------------------------------------------------------------------------
	'''
	def hideWidget(self,widget):
		widget.pi = widget.place_info()
		widget.place_forget();

	'''
	--------------------------------------------------------------------------------
		Desc: Display the Widget
	--------------------------------------------------------------------------------
	'''
	def showWidget(self,widget):
		if hasattr(widget, 'pi'):
			widget.place(widget.pi);
