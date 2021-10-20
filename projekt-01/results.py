import cv2
import tkinter

class Base(object):
  def __init__(self, image, title):
    self.image = image
    self.title = title
  
  def render(self) -> None:
    pass

  def show_img(self) -> int:
    # get screen resolution
    root = tkinter.Tk()
    root.withdraw()
    WIDTH, HEIGHT = root.winfo_screenwidth(), root.winfo_screenheight()

    # draw image
    img = cv2.imread(self.image)

    if img.shape[1] >= img.shape[0]: # width is bigger
      calc_width = 720
      while calc_width > WIDTH:
        calc_width -= 1
      calc_img_size = (calc_width, int(img.shape[0]*(calc_width/img.shape[1])))
    else: # height is bigger
      calc_height = 720
      while calc_height > HEIGHT:
        calc_height -= 1
      calc_img_size = (int(img.shape[1]*(calc_height/img.shape[0])), calc_height)

    img = cv2.resize(img, calc_img_size, interpolation = cv2.INTER_AREA)
    cv2.imshow(self.title, img)
    cv2.setWindowProperty(self.title, cv2.WND_PROP_TOPMOST, 1)
    cv2.moveWindow(self.title, int(WIDTH/2-calc_img_size[0]/2), int(HEIGHT/2-calc_img_size[1]/2))

    # loop to check for window close
    while True:
      k = cv2.waitKey(100)

      if k == 27 or k == 113:
        cv2.destroyAllWindows()
        break
      if cv2.getWindowProperty(self.title, cv2.WND_PROP_VISIBLE) < 1:
        break

    cv2.destroyAllWindows()
    return 0

class Quote(Base):
  def __init__(self, text, image):
    super().__init__(image, 'Quote')
    self.text = text
  
  def render(self) -> None:
    print('**** ' + self.text + ' ****')
    self.show_img()

class Cute(Base):
  def __init__(self, image):
    super().__init__(image, 'Meiiiiii')
  
  def render(self) -> None:
    self.show_img()