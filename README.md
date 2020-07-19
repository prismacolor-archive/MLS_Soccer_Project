# soccer

This script was created in an attempt to see which factors determine who wins in MLS matches. The data used were the general stats from the 2019 regular and post seasons.
The stats used were passing accuracy, shots on goal, corners, time of possession, fouls, red cards, and offsides. The initial analysis was done using Tableau visualizations,
located here: https://public.tableau.com/profile/tee8225#!/vizhome/Soccer_Sheets/MLSSnapshot?publish=yes. 

The initial model was done with all stats, and removed nonessential information such as name of team, date of game, season (regular or post) and opponent. The models chosen
were the decision trees and the random forest. The decision tree performed poorly, around 38% prediction rate. The random forest did slightly better at 49%. 

I then ran a second model, removing fouls, offsides, and red cards, as I wanted to see if they were causing any noise in the data. The results were the same, which suggests 
that these stats are not really essential in determining the chances of a win. Fouls and offsides, that makes sense. Red cards may factor in, but the reality is there are not 
that many games with red cards so it is hard to say whether playing a man down has a direct effect. I will say in one example, there was a team who got two red cards and still
performed fairly well. 

Another stat that is a little grey is the pass accuracy, there really wasn't that much of a range between teams in regards to the numbers here, so on the one hand, you'd think 
it would factor in and increase the chances of a win, but the numbers seem to suggest otherwise. I wonder, however, if this is something where if you perform particularly poorly 
one game, if that has more of an effect than performing well. In a comparison between the league champs (Seattle) and the team with the most losses (Cincinnati), you can clearly
see some differences in the stats, mainly in corners and shots on goal, and a pipeline between corners, shots taken, and goals scored, does seem to inidcate that corners and
shots on goal due have some weight when it comes to winning, it's just not clear from my project how much. 

Overall the stats used didn't seem to provide a strong foundation for predicting wins. There probably needs to be some additional stats, but at this time I am unsure what those 
might be from a numerical standpoint. As someone who has played soccer I would consider things like positioning/formation, for example running a 4-4-2 or 3-3-4. I'd also look at 
average speed of players, particularly strikers, and quality of goalkeeping. I'd also wonder if the overall level of experience on a team contributes to more wins. I'm sure some
would argue that coaching style should also be considered, but not sure how we would numerically quantify this. 

This was more an exploratory project, to focus on the actual analysis of this particular problem, both through the use of Tableau and scikit-learn modeling. I may do a revamp of 
the project where I incorporate more data from other seasons, and may look into quantifying some of these other stats. Thanks for reading, and feel free to play around with this.

Ciao!
