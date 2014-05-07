#coding:utf-8
import win32api,time
import win32con
import win32gui

from PIL import ImageGrab
import os
import Image
import time

# 获取屏幕截图
def getpng():
	time.sleep(2)
	im= ImageGrab.grab()
	im.save('E:\\program\\python\\pictrue\\ext.png','PNG')
	print "获取图片成功"

#获取鼠标位置
def get_mouse():
	(x,y) = win32gui.GetCursorPos()
	print (x,y)
	return (x,y)

#鼠标点击
def mousekey(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
	time.sleep(1)
	print "已经点击"
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

#查找图片中的小红点
def getrandom():
	im = Image.open('E:\\program\\python\\pictrue\\ext.png')
	rgb_im = im.convert('RGB')

	x = 1

	while (x <= 1300):
		y=1
		while(y <= 700):
			(r,g,b) = rgb_im.getpixel((x,y))
			if (r,g,b) == (255,0,0):
			#print r,g,b
				print "yes"
				print x, y
				mousekey(x,y)
				y=y+600
				x=x+1000	
			else:
				pass
				#print "not find"
			y=y+1
		x=x+1
	return x,y

def keyboard():
    #按下Ctr+W
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(87,0,0,0)
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(87,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(1)
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)

def keyboard_1():
 	win32api.keybd_event(34,0,0,0)
 	win32api.keybd_event(34,0,win32con.KEYEVENTF_KEYUP,0)

def click():
	'''
	x = 500
	while (x <= 1366):
		y=200
	#print rgb_im.getpixel((498, 324))

		while(y <= 768):
			mousekey(934, 255)
			try:
				getpng()

				a,b = getrandom(RED)
				time.sleep(3)
				mousekey(a,b)
				print a,b
				#time.sleep(10)
			except:
				print "no red"
				keyboard()
			y=y+600
		x=x+100
		'''
	
	for (x,y) in click_position:
		mousekey(x,y)
		try:
			getpng()
			time.sleep(3)
			getrandom()
		
		#mousekey(a,b)

			print "点击位置"
			time.sleep(20)
			keyboard()
			time.sleep(2)

		except:
			print "点击失败"
	keyboard_1()
	time.sleep(1)
	
	for (x,y) in click_position_2:
		mousekey(x,y)
		try:
			getpng()
			time.sleep(3)
			getrandom()
		
		#mousekey(a,b)

			print "点击位置"
			time.sleep(20)
			keyboard()
			time.sleep(2)

		except:
			print "点击失败"



def main():

	click()
	time.sleep(10)
	#x,y = getrandom(RED)
	#mousekey(x,y)
	keyboard()



if __name__ == '__main__':
	time.sleep(3)
	#main()
	RED = (255,0,0)
	HUAN = (255,255,153)
	click_position = ((580,276),(781, 276),(994,276),
						(580,382),(794,382),(994,382),
						(580,480),(794,480),(994, 482),
						(580,582),(794,582),(994, 582),
						
						
						(580,710),(761, 710),(994,710))
	click_position_2 =((584,296),
						(584, 416),(763, 411),(994,411),
						(540, 463))
	click()
