#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import pytesseract


# In[2]:


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# In[3]:


img = cv2.imread("C:\python\exp\Screenshot_2020-07-12-12-05-13-99.jpg")


# In[4]:


cv2.imshow("img",img)


# In[5]:


text = pytesseract.image_to_string(img)
print(text)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




