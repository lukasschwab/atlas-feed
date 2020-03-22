![Photograph of Konrad Wachsmann's USAF Hangar work.](./static/wachsmann.jpg)

# atlas-feed

This is a hacked-together JSON feed generator for [Atlas of Places](https://www.atlasofplaces.com); it naïvely processes their HTML, so I expect it to break eventually.

## Resources

+ [The feed is live here.](https://atlas-feed-dot-arxiv-feeds.appspot.com/)
+ [`arxiv-feeds`](https://github.com/lukasschwab/arxiv-feeds) does similar work, but in a more general way.

An example of the raw HTML structure being processed into an item:

```html
<a href="/cinema/dr-strangelove/">
  <div>
    <em></em>
    <img
      alt="Stanley Kubrick: Dr. Strangelove"
      class="lazy"
      data-src="https://www.atlasofplaces.com/atlas-of-places-thumbnails/_thumbnail/ATLAS-OF-PLACES-STANLEY-KUBRICK-DR-STRANGELOVE-IMG-5.jpg"
    />
  </div>
  <span>
    <small>Stanley Kubrick</small>
    <br/>
    Dr. Strangelove
  </span>
</a>
```
