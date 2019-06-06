'''
Contains configuration settings for html exporter
'''

c.TagRemovePreprocessor.remove_input_tags.add("to_remove")
c.TagRemovePreprocessor.remove_cell_tags.add("remove_cell")

exporter_settings = {
    'exclude_input_prompt' : True,
    'exclude_output_prompt' : True,
}
