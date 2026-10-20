import pygame
import math
import os
import time
import random



pygame.init()
Width = 1000
Hieght = Width/math.sqrt(6)*2
wn = pygame.display.set_mode((Width,Hieght))

class Point:
    def __init__(self,x,y,z,ID = None):
        self.Xpos = x
        self.Ypos = y
        self.Zpos = z
        self.ID = ID

    def getID(self):
        return self.ID

    def getXpos(self):
        return self.Xpos
    def getYpos(self):
        return self.Ypos
    def getZpos(self):
        return self.Zpos

    def setXpos(self,NewXpos):
        self.Xpos = NewXpos
    def setYpos(self,NewYpos):
        self.Ypos = NewYpos
    def setZpos(self,NewZpos):
        self.Zpos = NewZpos

    def printXpos(self):
        print(self.Xpos)
    def printYpos(self):
        print(self.Ypos)
    def printZpos(self):
        print(self.Zpos)

    def displayPoint(self,player):
        player.DisplayPoint(self)


class Cube(Point):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius
        point1 = Point(x+radius,y+radius,z+radius,"1")
        point2 = Point(x-radius,y+radius,z+radius,"2")
        point3 = Point(x-radius,y-radius,z+radius,"3")
        point4 = Point(x+radius,y-radius,z+radius,"4")
        point5 = Point(x+radius,y+radius,z-radius,"5")
        point6 = Point(x-radius,y+radius,z-radius,"6")
        point7 = Point(x-radius,y-radius,z-radius,"7")
        point8 = Point(x+radius,y-radius,z-radius,"8")
        self.points = [point1,point2,point3,point4,point5,point6,point7,point8]
        self.polygons = {(random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point2,point3,point4],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point2,point6,point5],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point2,point3,point7,point6],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point4,point8,point5],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point3,point4,point8,point7],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point5,point6,point7,point8]}

    def getRadius(self):
        return self.radius
    def setRadius(self,newRadius):
        self.radius = newRadius
    def printRadius(self):
        print(self.radius)

    def getPoints(self):
        return self.points
    def printPoints(self):
        print(self.points)

    def getPolygons(self):
        return self.polygons.items()
    def printPolygons(self):
        print(self.polygons.items())

    def getPolyColors(self):
        return self.polygons.keys()
    def printPolyColors(self):
        print(self.polygons.keys())

    # def calculatePlace(self,point):
    #     X,Y,Z = point.getXpos(),point.getYpos(),point.getZpos()
    #     Xfc,Yfc,Zfc = self.getXpos()-X,self.getYpos()-Y,self.getZpos()-Z
    #     if Zfc >= 0:
    #         Zfc=0.01
    #     RatioSumX = (-Zfc-Xfc)/-Zfc
    #     RatioSumY = (-Zfc-Xfc)/-Zfc
    #     return (Width/2 - RatioSumX,RatioSumY)
    
    def displayNonSolidVersion(self,player):
        for p1 in self.getPoints():
            player.DisplayPoint(p1)
            # print(player1.calculatePlace(p1))
    def displaySolidVersion(self,player):
        def CADP(x):
            return player.calculateAverageDistanceOfPolygon(x,player)*-1
        pts=sorted(self.getPolygons(),key = CADP)
        # print([[[y.getXpos(),y.getYpos(),y.getZpos()] for y in x] for x in pts])
        # print([[y.getID() for y in x] for x in pts])
        # print([player.calculateAverageDistanceOfPolygon(x,player) for x in pts])
        
        for p1 in pts:
            # print(p1)
            player.DisplayPolygon(p1[1],p1[0])

class T(Point):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius
        point1 = Point(x,y+radius,z,"1")
        point2 = Point(x-radius,y+radius,z+radius,"2")
        point3 = Point(x,y-radius,z+radius,"3")
        point4 = Point(x+radius,y,z+radius,"4")
        self.points = [point1,point2,point3,point4]
        self.polygons = {(random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point2,point3],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point2,point4],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point2,point3,point4],
                         (random.randint(0,255),random.randint(0,255),random.randint(0,255)):[point1,point3,point4]}

    def getRadius(self):
        return self.radius
    def setRadius(self,newRadius):
        self.radius = newRadius
    def printRadius(self):
        print(self.radius)

    def getPoints(self):
        return self.points
    def printPoints(self):
        print(self.points)

    def getPolygons(self):
        return self.polygons.items()
    def printPolygons(self):
        print(self.polygons.items())

    def getPolyColors(self):
        return self.polygons.keys()
    def printPolyColors(self):
        print(self.polygons.keys())
    
    def displayNonSolidVersion(self,player):
        for p1 in self.getPoints():
            player.DisplayPoint(p1)
            # print(player1.calculatePlace(p1))
    def displaySolidVersion(self,player):
        def CADP(x):
            return player.calculateAverageDistanceOfPolygon(x,player)*-1
        pts=sorted(self.getPolygons(),key = CADP)
        # print([[[y.getXpos(),y.getYpos(),y.getZpos()] for y in x] for x in pts])
        # print([[y.getID() for y in x] for x in pts])
        # print([player.calculateAverageDistanceOfPolygon(x,player) for x in pts])
        
        for p1 in pts:
            # print(p1)
            player.DisplayPolygon(p1[1],p1[0])

class Player(Point):
    def __init__(self):
        super().__init__(Width/2,Hieght/2,0)
        self.Xrotation = 0
        self.Yrotation = 0

    def getXRotation(self):
        return self.Xrotation
    def setXRotation(self,newXRotation):
        self.Xrotation = newXRotation
    def printXRotation(self):
        print(self.Xrotation)

    def getYRotation(self):
        return self.Yrotation
    def setYRotation(self,newYRotation):
        self.Yrotation = newYRotation
    def printYRotation(self):
        print(self.Yrotation)

    def calculatePlace(self,point):
        X,Y,Z = point.getXpos(),point.getYpos(),point.getZpos()
        Xfc,Yfc,Zfc = self.getXpos()-point.getXpos(),self.getYpos()-point.getYpos(),self.getZpos()-point.getZpos()
        def leftoverextra():
            # R = math.sqrt(Zfc**2+Xfc**2)
            # ta = -math.degrees(math.asin(Zfc/R))+self.getXRotation()%360
            # zm=-1
            # xm=1
            # print(ta," ",Zfc," ",Yfc," ",Xfc," ",R)
            # if -Zfc<0:
            #     if -Xfc<0:
            #         ta+=180
            #         xm=-1
            #         zm=1
            #     else:
            #         ta=360-ta
            #         zm=1
            # else:
            #     if -Xfc<0:
            #         ta=180-ta
            #         xm=-1
            #     else:
            #         ta+=0
            # # print(ta," ",Zfc," ",Xfc)
            # e=1
            # m=0
            # if Xfc<0:
            #     e=-1
            #     m=-100
            # Zfc = math.sin(math.radians(ta%360))*R*zm
            # Xfc = math.cos(math.radians(ta%360))*R*xm*e#+m
            # ################## Rotation for y
            # R = math.sqrt(Zfc**2+Yfc**2)
            # ta = -math.degrees(math.asin(Zfc/R))+self.getYRotation()%360
            # zm=-1
            # ym=1
            # print(ta," ",Zfc," ",Yfc," ",Xfc," ",R)
            # if -Zfc<0:
            #     if -Yfc<0:
            #         ta+=180
            #         ym=-1
            #         zm=1
            #     else:
            #         ta=360-ta
            #         zm=1
            # else:
            #     if -Yfc<0:
            #         ta=180-ta
            #         ym=-1
            #     else:
            #         ta+=0
            #         # print(ta," ",Zfc," ",Xfc)
            # e=1
            # m=0
            # if Yfc<0:
            #     e=-1
            #     m=-100
            # Zfc = math.sin(math.radians(ta%360))*R*zm
            # Yfc = math.cos(math.radians(ta%360))*R*ym*e#+m
            # print(ta," ",Zfc," ",Yfc," ",Xfc," ",R)
            return

        R = math.sqrt(Zfc**2+Xfc**2)
        a = (self.getXRotation()+90)%360
        Zfc = math.sin(a)*R
        Xfc = math.cos(a)*R
        if Zfc == 0:
            Zfc=0.01
        RatioSumX = (-Zfc-Xfc)/(-Zfc*2)
        RatioSumY = (-Zfc-Yfc)/(-Zfc*2)
        print(RatioSumX," ",RatioSumY,"\n")
        return (RatioSumX*Width,RatioSumY*Hieght)
    
    def calculateAverageDistanceOfPolygon(self,polypoints,player):
        SumOfPoints = 0
        # print(polypoints)
        for p in polypoints[1]:
            Xfc,Yfc,Zfc = p.getXpos()-player.getXpos(),p.getYpos()-player.getYpos(),p.getZpos()-player.getZpos()
            SumOfPoints += math.sqrt(Zfc**2+Xfc**2+Yfc**2)
        return SumOfPoints/len(polypoints)
    
    def calculateAverageDistanceOfShape(self,shape,player):
        Xfc,Yfc,Zfc = shape.getXpos()-player.getXpos(),shape.getYpos()-player.getYpos(),shape.getZpos()-player.getZpos()
        return math.sqrt(Zfc**2+Xfc**2+Yfc**2)
        
    def DisplayPoint(self,Point):
        pygame.draw.circle(wn,(255,255,255),self.calculatePlace(Point),3)#/math.log2(Point.getZpos()))
    def DisplayPolygon(self,Points,color):
        # print(Points)
        pts=[self.calculatePlace(x) for x in Points]
        # pygame.draw.polygon(wn,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),pts)
        pygame.draw.polygon(wn,color,pts)

player1 = Player()
cube = Cube(300,200,50,20)
shapes = [Cube(200,700,50,20),Cube(400,700,30,10),Cube(400,200,100,20),Cube(1200,200,500,490)]
# points = [Point(Width/2-100,Hieght/2-200,5),Point(Width/2-100,Hieght/2-200,10),Point(Width/2-100,Hieght/2-200,20),Point(Width/2-100,Hieght/2-200,30),Point(Width/2-100,Hieght/2-200,40),Point(Width/2-100,Hieght/2-200,50),Point(Width/2-100,Hieght/2-200,60),Point(Width/2-100,Hieght/2-200,70),Point(Width/2-100,Hieght/2-200,80),Point(Width/2-100,Hieght/2-200,90)]
running = True

while running == True:
    # time.sleep(0.05)
    wn.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    mouse = pygame.mouse
    # print(keys[pygame.K_w])
    MoveMultiplyer = 1
    if keys[pygame.K_LSHIFT]:
        MoveMultiplyer = 20
    if keys[pygame.K_w]:
        player1.setZpos(player1.getZpos()+5*MoveMultiplyer*math.cos(math.radians(player1.getXRotation())))
        player1.setXpos(player1.getXpos()+5*MoveMultiplyer*math.sin(math.radians(player1.getXRotation())))
    if keys[pygame.K_s]:
        player1.setZpos(player1.getZpos()-5*MoveMultiplyer*math.cos(math.radians(player1.getXRotation())))
        player1.setXpos(player1.getXpos()-5*MoveMultiplyer*math.sin(math.radians(player1.getXRotation())))
    if keys[pygame.K_d]:
        player1.setZpos(player1.getZpos()+5*MoveMultiplyer*math.sin(math.radians(180-player1.getXRotation()))*-1)
        player1.setXpos(player1.getXpos()+5*MoveMultiplyer*math.cos(math.radians(180-player1.getXRotation()))*-1)
    if keys[pygame.K_a]:
        player1.setZpos(player1.getZpos()-5*MoveMultiplyer*math.sin(math.radians(180-player1.getXRotation()))*-1)
        player1.setXpos(player1.getXpos()-5*MoveMultiplyer*math.cos(math.radians(180-player1.getXRotation()))*-1)
    if keys[pygame.K_SPACE]:
        player1.setYpos(player1.getYpos()-5*MoveMultiplyer)
    if keys[pygame.K_LCTRL]:
        player1.setYpos(player1.getYpos()+5*MoveMultiplyer)
    if keys[pygame.K_z]:
        player1.setXRotation(player1.getXRotation()-0.01*MoveMultiplyer)
    if keys[pygame.K_x]:
        player1.setXRotation(player1.getXRotation()+0.01*MoveMultiplyer)
    if keys[pygame.K_c]:
        player1.setYRotation(player1.getYRotation()+0.01*MoveMultiplyer)
    if keys[pygame.K_v]:
            player1.setYRotation(player1.getYRotation()-0.01*MoveMultiplyer)
    # player1.setXRotation(player1.getXRotation()+(Width/2-mouse.get_pos()[0])*0.02)
    # player1.setYRotation(player1.getYRotation()+(Hieght/2-mouse.get_pos()[1])*0.02)

    def CADP(x):
        return player1.calculateAverageDistanceOfShape(x,player1)*-1
    shapes=sorted(shapes,key = CADP)
    for s1 in shapes:
        # s1.printPolyColors()
        # s1.printPolygons()
        s1.displaySolidVersion(player1)
        # for p1 in s1.getPoints():
            # player1.DisplayPoint(p1)
            # print(player1.calculatePlace(p1))
        # print()
    ####################################################
    # player1.printXpos()
    # wn.fill((255,255,255),[x/20,y/20,x*18/20,y*18/20])
    ####################################################
    mouse.set_pos(Width/2,Hieght/2)
    pygame.display.flip()
print(Hieght/2)
# print(-1%360)
# [
# [[420, 220, 50], [380, 220, 50], [380, 180, 50], [420, 180, 50]],
# [[420, 220, 50], [380, 220, 50], [380, 220, 10], [420, 220, 10]],
# [[380, 220, 50], [380, 180, 50], [380, 180, 10], [380, 220, 10]],
# [[420, 220, 50], [420, 180, 50], [420, 180, 10], [420, 220, 10]],
# [[380, 180, 50], [420, 180, 50], [420, 180, 10], [380, 180, 10]],
# [[420, 220, 10], [380, 220, 10], [380, 180, 10], [420, 180, 10]]
# ]