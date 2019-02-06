#	llpdf - Tool to minify PDF files.
#	Copyright (C) 2016-2016 Johannes Bauer
#
#	This file is part of llpdf.
#
#	llpdf is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; this program is ONLY licensed under
#	version 3 of the License, later versions are explicitly excluded.
#
#	llpdf is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with llpdf; if not, write to the Free Software
#	Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#	Johannes Bauer <JohannesBauer@gmx.de>
#

import llpdf.filters
from .PDFDocument import PDFDocument
from .PDFWriter import PDFWriter
from .PDFReader import PDFReader
from .Measurements import Measurements
from .Logging import configure_logging
from llpdf.types.PDFName import PDFName
from llpdf.types.PDFString import PDFString
from llpdf.img.PDFExtImage import PDFExtImage
from llpdf.highlvl.PDFFunctions import HighlevelPDFFunctions
from llpdf.highlvl.PDFImageFunctions import HighlevelPDFImageFunctions, PDFImageFormatter

__RELEASE_VERSION = 0
__GIT_VERSION = 1
VERSION_TUPLE = (0, 1, __GIT_VERSION)
VERSION_INT = sum(value << (pos * 8) for (pos, value) in enumerate(reversed(VERSION_TUPLE)))
VERSION = "%d.%02d.%02d" % VERSION_TUPLE
