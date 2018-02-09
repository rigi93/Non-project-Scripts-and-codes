-- **********************a*****************************

select sname, age
from sailors;
-- **********************b*****************************

select *
from sailors
where rating > 7;
-- **********************c*****************************

select sname
from Sailors natural join Reserves natural join Boats
where bid=103;
-- **********************d*****************************

select distinct r.sid
from  Reserves r, Boats b 
where r.bid=b.bid and color='red';
-- **********************e*****************************

select s.sname
from Sailors s, Reserves r, Boats b
where s.sid=r.sid and r.bid=b.bid and color='red';
-- **********************f*****************************

select s.sname
from Sailors s, Reserves r
where s.sid=r.sid and r.bid is not null;
-- **********************g*****************************

select sname 
from Sailors natural join Reserves natural join Boats 
where color='red' or color='green';
-- **********************h*****************************

select distinct s.sname
from Sailors s, Reserves r, Boats b
where s.sid=r.sid and r.bid=b.bid and b.color=('red' and 'green');
-- **********************i*****************************

select s.sid
from Sailors s, Reserves r, Boats b
where s.sid=r.sid and r.bid=b.bid and b.color=('red')
and s.sid not in
(select s.sid
from Sailors s, Reserves r, Boats b
where s.sid=r.sid and r.bid=b.bid and b.color =('green'));
-- **********************j****************************

select s.sname
from Sailors s
where s.sid not in
(select s.sid
from Sailors s, Reserves r, Boats b
where s.sid=r.sid and r.bid=b.bid and b.bid=103);
-- **********************k****************************

select s.sname
from Sailors s
where s.rating > ( select min(s.rating)
from Sailors s
where s.sname='horatio');
-- **********************l****************************

select s.sname
from Sailors s
where s.rating > ( select max(s.rating)
from Sailors s
where s.sname='horatio');
-- ***********************m***************************

select s.sname
from Sailors s
where
NOT 
EXISTS
 ( select b.bid
from  Boats  b
where 
NOT  EXISTS
 ( select r.bid
from Reserves r
where r.bid = b.bid
and
r.sid = s.sid
)
 );
-- ***********************n**************************

select avg(s.age)
from Sailors s
where s.rating = 10;
-- *******************o******************************

select s.sname, s.age
from Sailors s
where s.age = (select max(s.age)
from Sailors s );
-- ********************p*****************************

select s.rating, MIN(s.age) AS mage
from Sailors s
where s.age > 18 
group by s.rating
having COUNT(*)>1;
-- *******************q******************************
select s.sid, s.sname, b.bname
from Sailors s LEFT OUTER JOIN Reserves r ON r.sid = s.sid LEFT OUTER JOIN Boats b ON r.bid = b.bid
ORDER BY s.sid;
