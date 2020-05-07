import pygame
import os



class Sprite:


    def __init__(self, spritePath:str, *files):
        self.spritePath=spritePath
        self.sprites=os.listdir(spritePath)
        counter=0
        while counter<len(self.sprites):
            x=self.sprites[counter].split('.')[-1]
            if x!='png' and x!='jpg':
                self.sprites.pop(counter)
            else:
                counter+=1
        if len(files)>0:
            counter=0
            while counter<len(self.sprites):
                if not self.sprites[counter] in files:
                    self.sprites.pop(counter)
                else:
                    counter+=1
        for i in range(len(self.sprites)):
            self.sprites[i]=self.spritePath+'/'+self.sprites[i]
        self.images=[]
        for image in self.sprites:
            self.images.append(pygame.image.load(image))

    def __len__(self):
        return len(self.images)

    def setSpritePath(self, spritePath, *files):
        self.spritePath=spritePath
        self.sprites=os.listdir(spritePath)
        counter=0
        while counter<len(self.sprites):
            x=self.sprites[counter].split('.')[-1]
            if x!='png' and x!='jpg':
                self.sprites.pop(counter)
            else:
                counter+=1
        if len(files)>0:
            counter=0
            while counter<len(self.sprites):
                if not self.sprites[counter] in files:
                    self.sprites.pop(counter)
                else:
                    counter+=1
        for i in range(len(self.sprites)):
            self.sprites[i]=self.spritePath+'/'+self.sprites[i]
        self.images=[]
        for image in self.sprites:
            self.images.append(pygame.image.load(image))

    def getSpritePath(self):
        return self.spritePath
    
    def getSprite(self, num):
        return self.images[num]


pygame.init()
