"""
document.py
Module that creates output document of different types
Created by Adam Harney
Nov 28, 2018
"""

import webbrowser
from fpdf import FPDF
from datetime import datetime
from os import path


class DocumentCreator:
    """
    Provides functions to create different types of documents
    """

    def create_pdf(direction_dict):
        """
        Creates a pdf document with the data retrieved from Google Maps
        direction_dict: dictionary of strings and lists with following keys:
            start_address
            end_address
            distance
            duration
            duration_in_traffic
            travel_mode
            instructions
            step_distance
        Returns: the full path plus the file name in one string
        """
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 14)
        pdf.multi_cell(180, 10, 'Directions from '
                       + direction_dict['start_address'][0] + ' to '
                       + direction_dict['end_address'][0])
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(180, 10, 'Distance: ' + direction_dict['distance'][0])
        pdf.multi_cell(180, 10, 'Duration: ' + direction_dict['duration'][0])
        pdf.multi_cell(180, 10, '')
        for index in range(len(direction_dict['instructions'])):
            pdf.set_font('Arial', '', 12)
            pdf.multi_cell(180, 5, direction_dict['instructions'][index])
            pdf.set_font('Arial', '', 10)
            pdf.multi_cell(180, 5,
                           direction_dict['step_distance'][index]['text'])
            pdf.multi_cell(180, 5, '')
        file_name = ('directions' + '{:%Y_%m_%d}'.format(datetime.now())
                     + '.pdf')
        full_file_path = path.join(path.join(path.expanduser('~')), file_name)
        pdf.output(full_file_path, 'F')

        return full_file_path

    def open_document(full_file_path):
        """
        Opens previously created document.
        """
        webbrowser.open_new(full_file_path)
