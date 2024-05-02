SELECT _name AS user,
       substr(day, 6, 2) AS month,
       sum(_clicks) AS nmb_of_clicks
FROM WebsiteStatisticsData
GROUP BY _name, substr(day, 6, 2);
