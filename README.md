# BookDrop
Pulling keepa data using their api then finding which books would be the best to buy for arbitrage

The Process as it now stands :
Use the links to perform a product search on Keepa.com
Download the ASINS


Product Search :
Used Price - $0-7.49, but 90 day avg $12+
Sales Rank - 180 days avg 0-7 mil
List Price - current and 180 avg $50+
Category - Books

Another one - 
Used Price - $0-3.50, but 180 avg $5+
Sales Rank - current, 30 days avg, 90 days, & 180 days avg all under 7 mil
List Price - $40+
Category - Books

Used price used to be higher, but now it's lower
List price is high (or x % greater than current used price)
Sales rank isn't crazy high

Take those ASINS plug them into the excel sheet-o-rama 
Put in 80 for empty data in List, new price, and new avg
Delete books that don't have a Sales Rank avg, min, or max

Do the VLook ups to see how it all ranks
SR current - 2
90 day avg - 4
SR Min - 2
SR max - 2
SR avg for selected dates - 10
Cur List price
Cur new price
new averge for dates
(total 109)

Add up all the values, weighted average between the two years, only look at books above a score of 67
Check to see which ASINS have already been checked before (But if its a good buy, its a good buy right???)

