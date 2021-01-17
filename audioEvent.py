import datetime

class AudioEvent:

  def __init__(self, days, times, name, description, mediaUrl):
    self.days = days
    self.times = times
    self.name = name
    self.description = description
    self.mediaUrl = mediaUrl

    self.today = datetime.datetime.today().weekday()



