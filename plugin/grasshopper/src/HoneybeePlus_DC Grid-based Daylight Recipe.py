# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# This file is part of Honeybee.
#
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""
Daylight Coefficient Grid-based Daylight Recipe.
Use this recipe to set up annual daylight analysis.

-

    Args:
        _skyMTX: A sky matrix or a sky vector. Find honeybee skies under 02::Daylight::Light Sources.
        _analysisGrids: A list of Honeybee analysis grids.
        _analysisType_: Analysis type. [0] illuminance(lux), [1] radiation (kwh),
            [2] luminance (Candela).
        _radiancePar_: Radiance parameters for Grid-based analysis. Find Radiance
            parameters node under 03::Daylight::Recipes.
        reuseDaylightMTX_: 
    Returns:
        readMe!: Reports, errors, warnings, etc.
        analysisRecipe: Annual analysis recipe. Connect this recipe to Run Radiance
            Analysis to run a annual analysis.
"""

ghenv.Component.Name = "HoneybeePlus_DC Grid-based Daylight Recipe"
ghenv.Component.NickName = 'DCoeffGBRecipe'
ghenv.Component.Message = 'VER 0.0.01\nDEC_03_2016'
ghenv.Component.Category = "HoneybeePlus"
ghenv.Component.SubCategory = '03 :: Daylight :: Recipe'
ghenv.Component.AdditionalHelpFromDocStrings = "2"

import honeybee
reload(honeybee.radiance.recipe.dc.gridbased)
try:
    from honeybee.radiance.recipe.dc.gridbased import DaylightCoeffGridBasedAnalysisRecipe
except ImportError as e:
    msg = '\nFailed to import honeybee. Did you install honeybee on your machine?' + \
            '\nYou can download the installer file from github: ' + \
            'https://github.com/ladybug-analysis-tools/honeybee-plus/tree/master/plugin/grasshopper/samplefiles' + \
            '\nOpen an issue on github if you think this is a bug:' + \
            ' https://github.com/ladybug-analysis-tools/honeybee-plus/issues'
        
    raise ImportError('{}\n\t{}'.format(msg, e))


if _skyMTX and _analysisGrids:
    analysisRecipe = DaylightCoeffGridBasedAnalysisRecipe(
        _skyMTX, _analysisGrids, _analysisType_, _radiancePar_, reuseDaylightMTX_)