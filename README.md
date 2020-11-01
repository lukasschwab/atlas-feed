![Photograph of Konrad Wachsmann's USAF Hangar work.](./static/wachsmann.jpg)

# atlas-feed

`atlas-feed` is a JSON Feed generator for [Atlas of Places](https://www.atlasofplaces.com); it naïvely processes their HTML, so I expect it to break eventually.

## Resources

+ `atlas-feed` is built with [`jsonfeed-wrapper`](https://github.com/lukasschwab/jsonfeed-wrapper) and [`jsonfeed`](https://github.com/lukasschwab/jsonfeed).
+ [The feed is live here.](https://us-central1-arxiv-feeds.cloudfunctions.net/atlas-feed)
+ Supports feeds for categories, e.g. [Cinema](https://us-central1-arxiv-feeds.cloudfunctions.net/atlas-feed/cinema).

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
