#!/usr/bin/python3

"""
these tests are archive.moe-oriented
"""

import unittest
import moesearch as foolz

def select_first_couple(dict_):
  return list(dict_.items())[0]

class TestIndex(unittest.TestCase):
  def setUp(self):
    self.a_index = foolz.index("a", 1)

  def test_workswithboardobj(self):
    self.r9k_index = foolz.index(foolz.parser.Board('r9k'), 5)
  
  def test_boardexception(self):
    self.assertRaises(foolz.exceptions.ArchiveException,
                      foolz.index,
                      #parameters
                      "welovewoxxy", 1
                    )
  
  def test_call_a(self):
    res = self.a_index
    self.assertIsInstance(res, dict)
    self.assertIsInstance(select_first_couple(res)[1], foolz.parser.IndexResult)
  
  def test_isrequestedboard(self):
    """ check the results are from the board we asked for """
    self.assertEqual(0, 
         sum(1 for post_num, post in self.a_index.items() if post.op.board.short_name != 'a')
         )

class TestThread(unittest.TestCase):
  def setUp(self):
    self.muh_thread = foolz.thread('co', 77173065)
  
  def test_workswithboardobj(self):
    foolz.thread(foolz.parser.Board('co'), 77173065)

  def test_isthatyou(self):
    self.assertEqual(77173065, int(self.muh_thread.op.thread_num))
    self.assertIsInstance(self.muh_thread, foolz.parser.Thread)

  def test_thread_isnota_indexresult(self):
    #http://stackoverflow.com/a/2267788
    self.assertRaises(AttributeError, lambda: self.muh_thread.omitted)
    self.assertRaises(AttributeError, lambda: self.muh_thread.images_omitted)

class TestPost(unittest.TestCase):
  def setUp(self):
    self.media_post      = foolz.post('fit', 34763974)
    self.no_media_post   = foolz.post('fit', 34767518)
    self.no_comment_post = foolz.post('a', 133062380)

  def test_workswithboardobj(self):
    foolz.post(foolz.parser.Board('fit'), 34763974)

  def test_isthatyou(self):
    """ check the response is the one we're looking for. """
    self.assertEqual('fit', self.media_post.board.short_name)
    self.assertEqual('fit', self.no_media_post.board.short_name)
    self.assertEqual(133062380, int(self.no_comment_post.num))
    self.assertEqual(34763974, int(self.media_post.num))
    self.assertEqual(34767518, int(self.no_media_post.num))
  
  def test_nomedia_hasattributes(self):
    """ don't crash when asking media data to a no-media post """
    self.assertIsInstance(self.no_media_post.media, foolz.parser.Media)
    self.assertEqual(None, self.no_media_post.media.media_link)
    self.assertEqual(None, self.no_media_post.media.exif)

  def test_media_data(self):
    """ check media data are correct for the media post """
    self.assertEqual("https://cdn2.desu-usergeneratedcontent.xyz/fit/image/1444/85/1444858212551.jpg", self.media_post.media.media_link)

  def test_no_comment(self):
    """ if a post has no comment, it has to have an image/webm! """
    self.assertEqual(None, self.no_comment_post.comment)
    self.assertNotEqual(None, self.no_comment_post.media.media_link)

class TestSearch(unittest.TestCase):
  def setUp(self):
    #we can't really omit the board
    self.muh_vampire_search = foolz.search(foolz.parser.Board('a'), subject='vampires')
    #more than one board works too!
    self.vampires_on_more_boards = foolz.search([
                                                foolz.parser.Board('a'),
                                                foolz.parser.Board('co')
                                                ],
                                                text='vampires')
    self.kek_on_r9k = foolz.search('r9k', text='kek')
  
    
  def test_aretheyvampires(self):
    self.assertEqual(0, sum(1 for post in self.muh_vampire_search if post.title.lower().count("vampires")==0))
    self.assertEqual(0, sum(1 for post in self.vampires_on_more_boards if post.comment.lower().count("vampires")==0))

  def test_gotsomething(self):
    self.assertNotEqual(0, len(self.muh_vampire_search))
    self.assertNotEqual(0, len(self.vampires_on_more_boards))

  def test_actuallyfrommoreboards(self):
    self.assertEqual(set(('a', 'co')), set(post.board.short_name for post in self.vampires_on_more_boards))

  def test_longerboardsnotsplitted(self):
    for post in self.kek_on_r9k:
      self.assertNotEqual('k', post.board.short_name)
      self.assertEqual('r9k', post.board.short_name)

class TestUtilities(unittest.TestCase):
  def setUp(self):
    self.cool_thread = foolz.thread('co', 77173065)

  def test_cangetmediaposts(self):
    self.assertNotEqual(0, len(list(foolz.media_in_thread(self.cool_thread))))
    #that test is waaaay too specific.
    #self.assertEqual(196, len(list(foolz.media_in_thread(self.cool_thread))))

  #TODO: add tests for differences between posts with and without OP media

  def test_nowebmthere(self):
    #/co/37108096 started in May 2012, and afaik webm wasn't supported
    mit_iter = foolz.media_in_thread(self.cool_thread)
    self.assertEqual(0, len(list(foolz.filter_by_type(mit_iter, ok_types=['webm']))))


if __name__ == "__main__":
  unittest.main()
