#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:dynamic,slots,utf8strings,new_style
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.protocol.TBase import TBase, TExceptionBase



class UserProfile(TBase):
  """
  Attributes:
   - uid
   - name
  """

  __slots__ = [ 
    'uid',
    'name',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'uid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
  )

  def __init__(self, uid=None, name=None,):
    self.uid = uid
    self.name = name

