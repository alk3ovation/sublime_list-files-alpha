import sublime, sublime_plugin, os

file_views = []

class ListOpenFilesAlphabeticallyCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      global file_views
      file_views = []
      for vw in self.view.window().views():
         if( vw.file_name() != None ):
            head, tail = os.path.split(vw.file_name())
            file_views.append(( tail, vw ) )
         else:
            file_views.append( ( vw.substr(vw.line(0) ), vw) )
      file_views.sort(key=lambda tup: tup[0]);
      #data.sort(key=lambda tup: tup[1])  // sorts in place

      self.view.window().show_quick_panel([x for (x, y) in file_views], self.on_chosen)

   def on_chosen(self, index):
      if index != -1:
         win = self.view.window()
         win.focus_view(file_views[index][1])