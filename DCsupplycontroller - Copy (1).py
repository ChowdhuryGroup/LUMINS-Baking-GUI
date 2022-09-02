import wx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas, NavigationToolbar2WxAgg as NavigationToolbar
import numpy as np
from os import getcwd, chdir, startfile, makedirs
from os.path import realpath,exists,join,abspath,dirname
import os,sys
from PIL import Image
import pandas as pd
import matplotlib.image as mpimg
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy.linalg import norm



class TopPanel(wx.Panel):
    
 
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)
        self.Buttonfile=wx.Button(self,-1,"Add data to file")
        self.addfilestext=wx.StaticText(self, -1,'Add new data to files',pos=(200,20))
        self.addtime=wx.StaticText(self, -1,'Add Time',pos=(200,35))
        self.addtime1=wx.TextCtrl(self, -1,pos=(350,35))
        self.addreflexobj=wx.StaticText(self, -1,'Add reflex obj temp',pos=(200,95))
        self.addreflexobj1=wx.TextCtrl(self, -1,pos=(350,95))
        self.addviewport=wx.StaticText(self, -1,'Add viewport',pos=(200,135))
        self.addviewport1=wx.TextCtrl(self, -1,pos=(350,135))
        self.addSTMhead=wx.StaticText(self, -1,'Add STM head',pos=(200,175))
        self.addSTMhead1=wx.TextCtrl(self, -1,pos=(350,175))
        self.addiongauge=wx.StaticText(self, -1,'Add ion gauge',pos=(200,215))
        self.addiongauge1=wx.TextCtrl(self, -1,pos=(350,215))
        self.addsputtergun=wx.StaticText(self, -1,'Add sputter gun',pos=(200,255))
        self.addsputtergun1=wx.TextCtrl(self, -1,pos=(350,255))
        self.addeheater=wx.StaticText(self, -1,'eheater',pos=(200,295))
        self.addeheater1=wx.TextCtrl(self, -1,pos=(350,295))                                
        self.addPressure=wx.StaticText(self, -1,'Pressure',pos=(200,335))
        self.addPressure1=wx.TextCtrl(self, -1,pos=(350,335))
        self.Buttonfile.Bind(wx.EVT_BUTTON,self.Addfile)

        os.chdir('C:\\Users\\spmuser\\Desktop')
            #os.makedirs('Baking_tempevolution_on_LUMINS')
            #os.chdir('C:\\Users\\spmuser\\Desktop\\Baking_tempevolution_on_LUMINS')
        if os.path.exists('parts_temp.csv'):
            pass
        else:
            parts_temp = pd.DataFrame(columns=['Time','reflex obj1','viewport2','STM head3','ion gauge port4','sputter gun port5','eheater port6','Pressure'])
            parts_temp.to_csv('parts_temp.csv', index=False, na_rep='Unknown')
        def OnEnterPressed1(self,event):
            msg1=(str(self.addtime1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed2(self,event):
            msg2=(str(self.addreflexobj1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed3(self,event):
            msg3=(str(self.addviewport1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed4(self,event):
            msg4=(str(self.addSTMhead1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed5(self,event):
            msg5=(str(self.addiongauge1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed6(self,event):
            msg6=(str(self.addsputtergun1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed7(self,event):
            msg7=(str(self.addeheater1.GetValue()))
            #wx.MessageBox(msg1)

        def OnEnterPressed8(self,event):
            msg8=(str(self.addPressure1.GetValue()))
            #wx.MessageBox(msg1)
            
        #self.addtime1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed1)
        #self.addreflexobj1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed2)
        #self.addSTMhead1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed3)
        #self.addviewport1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed4)
        #self.addiongauge1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed5)
        #self.addsputtergun1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed6)
        #self.addeheater1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed7)
        #self.addPressure1.Bind(wx.EVT_TEXT_ENTER,OnEnterPressed8)
        



    def Addfile(self,event):
        os.chdir('C:\\Users\\spmuser\\Desktop')
        temp_time_point = pd.DataFrame({'Time': [self.addtime1.GetValue()],
                   'reflex obj1': [self.addreflexobj1.GetValue()],
                  'viewport2': [self.addviewport1.GetValue()], 'STM head3': [self.addSTMhead1.GetValue()],'ion gauge port4': [self.addiongauge1.GetValue()],'sputter gun port5': [self.addsputtergun1.GetValue()],'eheater port6': [self.addeheater1.GetValue()],'Pressure': [self.addPressure1.GetValue()]})
        temp_time_point.to_csv('parts_temp.csv', mode='a', index=False, header=False)
    
        #self.Buttonfile.Bind(wx.EVT_BUTTON,self.Addfile)
        
            

         
        

class BottomPanel(wx.Panel):
    def Startevolution(self,event):
        #self.fig2, self.ax2 = plt.subplots(figsize=(3,3))
        #self.fig = plt.figure()
        #self.ax = self.fig.add_subplot(111, projection='3d')
        theta = np.linspace(0, 2 * np.pi, 201)
        phi = np.linspace(0,np.pi,201)
# definition of sphere:
        def sphere(diameter):
            x0 =diameter * np.outer(np.cos(theta),np.sin(phi))
            y0 = diameter * np.outer(np.sin(theta),np.sin(phi))
            z0 = diameter * np.outer(np.ones(201),np.cos(phi))
            return x0,y0,z0
# definition of cylinder for reflex obj port1:
        def port1(R): 
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([-8.9,14.4,-10.5])
            p1 = np.array([-17.8, 28.8, -21])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
                not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
# definition of cylinder for viewport2:
        def port2(R):  
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([-10.7, -14.32, -8.9])
            p1 = np.array([-21.4,-28.64,-17.8])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
               not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
# definition of cylinder for STM head3:
        def port3(R):
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([0, 0, 20])
            p1 = np.array([0, 0, 80])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
               not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
# definition of cylinder for ion gauge port4:
        def port4(R): 
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([7.7, -15.15, 10.5])
            p1 = np.array([15.4, -30.3, 21])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
               not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
# definition of cylinder for sputter gun port5:
        def port5(R): 
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([17.12, -9.85, 3])
            p1 = np.array([42.8, -24.625, 7.5])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
               not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
# definition of cylinder for eheater port6:
        def port6(R): 
            theta = np.linspace(0, 2 * np.pi, 201)
            p0 = np.array([9.39, 15.21, -8.96])
            p1 = np.array([28.17, 45.63, -26.88])
    #vector in direction of axis
            v = p1 - p0
    #find magnitude of vector
            mag = norm(v)
    #unit vector in direction of axis
            v = v / mag
    #make some vector not in the same direction as v
            not_v = np.array([1, 0, 0])
            if (v == not_v).all():
               not_v = np.array([0, 1, 0])
    #make vector perpendicular to v
            n1 = np.cross(v, not_v)
    #normalize n1
            n1 /= norm(n1)
    #make unit vector perpendicular to v and n1
            n2 = np.cross(v, n1)
    #surface ranges over t from 0 to length of axis and 0 to 2*pi
            t = np.linspace(0, mag, 201)
            phi = np.linspace(0,np.pi,201)
            t, theta = np.meshgrid(t, theta)
            X, Y, Z = [p0[i] + v[i] * t + R * np.sin(theta) * n1[i] + R * np.cos(theta) * n2[i] for i in [0, 1, 2]]
            return X,Y,Z
        x0,y0,z0=sphere(20)
        x1,y1,z1=port1(5)
        x2,y2,z2=port2(15)
        x3,y3,z3=port3(10)
        x4,y4,z4=port4(5)
        x5,y5,z5=port5(5)
        x6,y6,z6=port6(5)

    
    
        plt.ion()
        # Data Coordinates
        os.chdir('C:\\Users\\spmuser\\Desktop')
        results = pd.read_csv('parts_temp.csv')
        #while True:
        for i in range(len(results)):
            color_temp=[]
            temp1=results.iat[i,1]
            temp2=results.iat[i,2]
            temp3=results.iat[i,3]
            temp4=results.iat[i,4]
            temp5=results.iat[i,5]
            temp6=results.iat[i,6]
            temp=[temp1,temp2,temp3,temp4,temp5,temp6]
            for j in range(6):
                if temp[j] in range(0,25):
                   color_temp.append('grey')
                elif temp[j] in range(26,35):
                   color_temp.append('blue')
                elif temp[j] in range(36,45):    
                   color_temp.append('yellow')
                elif temp[j] in range(46,50):
                   color_temp.append('red')
                elif temp[j] in range(51,55):
                   color_temp.append('green')
                elif temp[j] in range(56,60):
                   color_temp.append('purple')
                elif temp[j] in range(61,65):
                   color_temp.append('black')
                elif temp[j] in range(66,70):
                   color_temp.append('orange')
                elif temp[j] in range(71,75):
                   color_temp.append('lightpink')
                elif temp[j] in range(76,80):
                   color_temp.append('aqua')
                elif temp[j] in range(81,85):
                   color_temp.append('plum')
                elif temp[j] in range(86,90):
                   color_temp.append('lime')
                elif temp[j] in range(91,95):
                   color_temp.append('salmon')
                else:
                   color_temp.append('tomato')
               
               
            

            self.ax.plot_surface(x0,y0,z0, color='magenta')
            self.ax.plot_surface(x1,y1,z1, color=color_temp[0])
            self.ax.plot_surface(x2,y2,z2, color=color_temp[1])
            self.ax.plot_surface(x3,y3,z3, color=color_temp[2])
            self.ax.plot_surface(x4,y4,z4, color=color_temp[3])
            self.ax.plot_surface(x5,y5,z5, color=color_temp[4])
            self.ax.plot_surface(x6,y6,z6, color=color_temp[5])
            self.ax.set_xticks([-100, 100])
            self.ax.set_yticks([-100,  100])
            self.ax.set_zticks([-100, 100])
            self.ax.set_title('%s'%results.iat[i,0]+'%s'%results.iat[i,7], loc='right')#,'&', results.iat[i,7] )
           #time.sleep(10)
            if os.path.exists('C:\\Users\\spmuser\\Desktop\\Baking evolution'):
               pass
            else:
               os.makedirs('C:\\Users\\spmuser\\Desktop\\Baking evolution')
            os.chdir('C:\\Users\\spmuser\\Desktop\\Baking evolution')
            self.ax.view_init(-8, -140)
            self.fig.savefig('%d.png'%i)
            self.canvas = FigureCanvas(self, 1, self.fig)
            self.sizer.Add(self.canvas,1,wx.EXPAND)
        #Time=results['Time'].tolist()
        #Pressure=results['Pressure'].tolist()
        #self.ax2.plot(Time, Pressure)
        #self.ax2.set_xlabel('Time')
        #self.ax2.set_ylabel('Pressure')
        #self.canvas2 = FigureCanvas(self, 1, self.fig2)
        #self.sizer.Add(self.canvas2,1,wx.EXPAND)
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)
        button2=wx.Button(self,-1,"Start evolution")
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(button2,1)
        self.SetSizer(self.sizer)
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        #button2.Bind()
        #img=Image.open('C:\\Users\\spmuser\\Desktop\\GUI py\\1.png')
        #img=mpimg.imread('C:\\Users\\spmuser\\Desktop\\GUI py\\1.png')
        #img.show()
        button2.Bind(wx.EVT_BUTTON,self.Startevolution)
        os.chdir('C:\\Users\\spmuser\\Desktop')
        self.ax.clear()


    

    def CreatePlot(self):
        self.fig1, self.ax1 = plt.subplots(figsize=(6, 1))
        self.fig1.subplots_adjust(bottom=0.5)
        self.cmap = mpl.colors.ListedColormap(['grey', 'blue', 'yellow', 'red', 'green', 'purple', 'black', 'orange', 'lightpink', 'aqua', 'plum', 'lime', 'salmon', 'tomato'])
        self.cmap.set_over('0.25')
        self.cmap.set_under('0.75')
        bounds = [1,25,35,45,50,55,60,65,70,75,80,85,90,95,100]
        self.norm = mpl.colors.BoundaryNorm(bounds, self.cmap.N)
        self.cb2 = mpl.colorbar.ColorbarBase(self.ax1, cmap=self.cmap,
                                norm=self.norm,
                                #boundaries=[0] + bounds + [13],
                                extend='both',
                                ticks=bounds,
                                spacing='proportional',
                                orientation='horizontal')
        self.cb2.set_label('Discrete intervals, some other units')
        self.canvas = FigureCanvas(self, 1, self.fig1)
            #self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.canvas,1,wx.EXPAND)
            #self.SetSizer(self.sizer)
        if os.path.exists('C:\\Users\\spmuser\\Desktop\\Baking evolution'):
           pass
        else:
            os.makedirs('C:\\Users\\spmuser\\Desktop\\Baking evolution')
        os.chdir('C:\\Users\\spmuser\\Desktop\\Baking evolution')

        self.fig1.savefig('Self-defined colorbar')


class bottomPRight(wx.Panel):
     def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent)
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        button3=wx.Button(self,-1,"Time-Pressure")
        self.sizer.Add(button3,1)
        self.SetSizer(self.sizer)
        button3.Bind(wx.EVT_BUTTON,self.TimePressure)
        self.fig2 = plt.figure()
        self.ax2 = self.fig2.add_subplot(111)
        self.ax2.clear()
     def TimePressure(self,event):
         os.chdir('C:\\Users\\spmuser\\Desktop')
         results = pd.read_csv('parts_temp.csv')
         #self.fig2 = plt.figure()
         #self.ax2 = self.fig2.add_subplot(111)
         Time=results['Time'].tolist()
         Pressure=results['Pressure'].tolist()
         self.ax2.plot(Time, Pressure)
         self.ax2.set_xlabel('Time')
         self.ax2.set_ylabel('Pressure')
         self.canvas2 = FigureCanvas(self, 1, self.fig2)
         self.sizer.Add(self.canvas2,1,wx.EXPAND)
         if os.path.exists('C:\\Users\\spmuser\\Desktop\\Baking evolution'):
            pass
         else:
             os.makedirs('C:\\Users\\spmuser\\Desktop\\Baking evolution')
         os.chdir('C:\\Users\\spmuser\\Desktop\\Baking evolution')
         self.fig2.savefig('Time-Pressure')
        
#class BottomP(wx.Panel):
      #def __init__(self,parent):
           #wx.Panel.__init__(self,parent=parent)

           
class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,parent=None, title='Baking evolution of LUMINS', size=(1000,1000))
        splitter=wx.SplitterWindow(self)
        vSplitter = wx.SplitterWindow(splitter)
               # SPLIT THE WINDOW
        top=TopPanel(splitter)
        #bottom=BottomP(splitter)
        #bottom=BottomPanel(splitter)
        splitter.SplitHorizontally(top,vSplitter)
        panelOne = BottomPanel(vSplitter)
        panelTwo = bottomPRight(vSplitter)
        vSplitter.SplitVertically(panelOne, panelTwo)
        splitter.SetMinimumPaneSize(500)
        vSplitter.SetMinimumPaneSize(500)
        panelOne.CreatePlot()
        
        
    

if __name__=='__main__':
    app=wx.App()
    frame=Main()
    frame.Show()
    app.MainLoop()
