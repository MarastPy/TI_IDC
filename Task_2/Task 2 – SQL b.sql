SELECT  _name, 
        substr(day, 6, 2) AS month,
    	round(sum(_clicks) * 100.0 / (SELECT sum(_clicks) FROM WebsiteStatisticsData), 2) || '%' AS percentage_share
FROM WebsiteStatisticsData
GROUP BY _name, substr(day, 6, 2);
