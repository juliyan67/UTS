class SingletonObject:
    # deklarasi privat object
    _singletonObject = None
 
    # Annotations from static method
    @staticmethod
    def getSingletonObjectInstance():
        # if the value of _singletonObject is None
        if SingletonObject._singletonObject is None:
            # object menjalankan instance
            SingletonObject._singletonObject = SingletonObject()
        # return nilai _singletonObject
        return SingletonObject._singletonObject
 
    # pengujian method _singletonObject merupakan instance atau bukan
    def getMessage(self):
        print (&quot;Hello I'm from singleton Object&quot;)
          
               

singletonObject = SingletonObject.getSingletonObjectInstance()
# memangil method test
singletonObject.getMessage()
