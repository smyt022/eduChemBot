### STARTUP ########################################################
import discord
import os
from discord.ext import commands
bot = commands.Bot(command_prefix="$")

## FUNCTIONS #######################################################

#Reads the properties File for an Element, and Displays it's Properties (all in one line)
##Reads the properties File for an Element, and Displays it's Properties (all in one line)
def getElementProperties(elementNumber):
  fileReader = open("properties.txt", 'r')
  
  for i in range (elementNumber - 1):
    fileReader.readline()
  
  return fileReader.readline()

#method to get molar mass from atomic number
def getMolarMass(elementNumber):
  #Gets the Properties of the Element
  properties = getElementProperties(elementNumber)

  #Isolate for the Molar Mass
  propertiesArr = properties.split()
  molarMass = propertiesArr[3]
  
  return molarMass
  
#Gets the Element's ID
def getElementID(userElement):
  
  #List of ELements
  elementArr = ['hydrogen', 'helium', 'lithium', 'beryllium', 'boron', 'carbon', 'nitrogen', 'oxygen', 'fluorine', 'neon', 'sodium', 'magnesium', 'aluminum', 'silicon', 'phosphorus', 'sulfur', 'chlorine', 'argon', 'potassium', 'calcium', 'scandium', 'titanium', 'vanadium', 'chromium', 'manganese', 'iron', 'cobalt', 'nickel', 'copper', 'zinc', 'gallium', 'germanium','arsenic', 'selenium', 'bromine', 'krypton', 'rubidium', 'strontium', 'yttrium', 'zirconium', 'niobium', 'molybdenum', 'technetium', 'ruthenium', 'rhodium', 'palladium', 'silver', 'cadmium', 'indium', 'tin', 'antimony', 'tellurium', 'iodine', 'xenon', 'cesium', 'barium', 'lanthanum', 'cerium', 'praseodymium', 'neodymium', 'promethium', 'samarium', 'europium', 'gadolinium', 'terbium', 'dysprosium', 'holmium', 'erbium', 'thulium', 'ytterbium', 'lutetium', 'hafnium', 'tantalum', 'tungsten', 'rhenium', 'osmium', 'iridium', 'platinum', 'gold', 'mercury', 'thallium', 'lead', 'bismuth', 'polonium', 'astatine', 'radon', 'francium', 'radium', 'actinium', 'thorium', 'protactinium', 'uranium', 'neptunium', 'plutonium', 'americium', 'curium', 'berkelium', 'californium', 'einsteinium', 'fermium', 'mendelevium', 'nobelium', 'lawrencium', 'rutherfordium', 'dubnium', 'seaborgium', 'bohrium', 'hassium', 'meitnerium', 'ununnilium', 'unununium', 'ununbium']

  #loop through list, return index+1 (atomic number)
  for i in range(112):
    if (userElement == elementArr[i]):
      return i + 1

  #If the Loop is Unable to Match the User's Input with an Element
  return -1
    
## COMMANDS ###############################################

#Returns the Molar Mass of a Desired Element
@bot.command(
  help = "Returns the molar mass of a provided element\nSyntax: $getMM <elementName> || <atomicNumber>",
  brief = "Return molar mass"
)
async def getMM (ctx, args):

  try:
    #Checks if the args are an integer. Else, will throw exception
    int(args) + 1

    #If the User Entered an Integer, Pass it Directly to the   
    #Function
    if int(args) > 0 and int(args) <= 112:
      #Print the Molar Mass
      await ctx.channel.send("Molar Mass: "+str(getMolarMass(int(args)))+"g/mol")
    else:
      #If the Atomic Number is Out of Bounds
      await ctx.channel.send("Atomic number is out of bounds")

  except ValueError:
    #If the User Entered a String, Match it to an Element's ID
    id = getElementID(str(args))
    if id == -1:
      #If Unable to Locate Element
      await ctx.channel.send("Element not Found")
    else:
      #Print the Molar Mass
      await ctx.channel.send("Molar Mass: "+str(getMolarMass(id))+"g/mol")

#Returns all Properties of the Element
@bot.command(
  help = "Returns the atomic number, symbol, name, and molar mass of an element\nSyntax: $getProp <elementName> || <atomicNumber>",
  brief = "Returns information about an element"
)
async def getProp (ctx, args):

  try:
    #Checks if the args are an integer. Else, will throw exception
    int(args) + 1

    #If the User Entered an Integer, Pass it Directly to the   
    #Function
    if int(args) > 0 and int(args) <= 112:
      #Print the Molar Mass
      await ctx.channel.send(getElementProperties(int(args)))
    else:
      #If the Atomic Number is Out of Bounds
      await ctx.channel.send("Atomic number is out of bounds")

  except ValueError:
    #If the User Entered a String, Match it to an Element's ID
    id = getElementID(str(args))
    if id == -1:
      #If Unable to Locate Element
      await ctx.channel.send("Element not Found")
    else:
      #Print the Molar Mass
      await ctx.channel.send(getElementProperties(id))
  
## SYSTEM ##################################################
#Running the bot
bot.run(os.environ['TOKEN'])